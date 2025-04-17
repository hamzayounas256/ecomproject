from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Products, Header,Detail
from decimal import Decimal
import json
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def header_create(request):
    if request.method != 'POST':
        return JsonResponse(
            {"message": "Method not allowed", "success": False},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    
    try:
        # Parse JSON data from request body
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse(
                {"message": "Invalid JSON data", "success": False},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Validate required fields
        required_header_fields = [
            'order_date', 'order_time', 'cust_name', 'cust_address',
            'cust_phone_no', 'cust_email', 'cust_nic', 'products'
        ]
        missing_header = [field for field in required_header_fields if field not in data]
        if missing_header:
            return JsonResponse(
                {"message": f"Missing header fields: {', '.join(missing_header)}", "success": False},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not isinstance(data['products'], list) or len(data['products']) == 0:
            return JsonResponse(
                {"message": "At least one product must be provided", "success": False},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        for product in data['products']:
            if 'product_code' not in product or 'quantity' not in product:
                return JsonResponse(
                    {"message": "Each product must have product_code and quantity", "success": False},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if not isinstance(product['quantity'], int) or product['quantity'] <= 0:
                return JsonResponse(
                    {"message": "Quantity must be a positive integer", "success": False},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        # Check if header with this email exists
        header = Header.objects.filter(cust_email=data['cust_email']).first()
        header_created = False

        if not header:
            # Create new header
            try:
                header = Header.objects.create(
                    order_date=data['order_date'],
                    order_time=data['order_time'],
                    cust_name=data['cust_name'],
                    cust_address=data['cust_address'],
                    cust_phone_no=data['cust_phone_no'],
                    cust_email=data['cust_email'],
                    cust_nic=data['cust_nic'],
                    total_qnty=0,
                    total_amount=Decimal('0.00'),
                    total_sale_amount=Decimal('0.00')
                )
                header_created = True
            except Exception as e:
                return JsonResponse(
                    {"message": f"Error creating order header: {str(e)}", "success": False},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        # Process products
        details = []
        for product_data in data['products']:
            try:
                product = Products.objects.get(id=product_data['product_code'])
            except Products.DoesNotExist:
                if header_created:
                    header.delete()
                return JsonResponse(
                    {"message": f"Product with ID {product_data['product_code']} not found", "success": False},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            quantity = product_data['quantity']
            
            if product.stock_qnty < quantity:
                if header_created:
                    header.delete()
                return JsonResponse(
                    {
                        "message": f"Insufficient stock for product {product.product_name}. Available: {product.stock_qnty}, Requested: {quantity}",
                        "success": False
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            discount = product.discount or Decimal('0.00')
            product_rate = product.product_rate
            product_amount = product_rate * quantity
            product_sale_rate = product_rate - discount
            product_sale_amount = product_sale_rate * quantity
            
            detail = Detail(
                order_no=header,
                product_code=product,
                product_name=product.product_name,
                product_rate=product_rate,
                product_qnty=quantity,
                product_amount=product_amount,
                product_sale_rate=product_sale_rate,
                product_sale_amount=product_sale_amount,
                product_img=product.product_img,
            )
            details.append(detail)
            
            product.stock_qnty -= quantity
            product.save()
        
        # Save details and update header totals
        Detail.objects.bulk_create(details)
        header.total_qnty += sum(d.product_qnty for d in details)
        header.total_amount += sum(d.product_amount for d in details)
        header.total_sale_amount += sum(d.product_sale_amount for d in details)
        header.save()
        
        return JsonResponse(
            {
                "message": "Order details added successfully to existing header" if not header_created else "Order created successfully",
                "success": True,
                "order_id": header.order_no,
                "total_quantity": header.total_qnty,
                "total_amount": str(header.total_amount),
                "total_sale_amount": str(header.total_sale_amount)
            },
            status=status.HTTP_201_CREATED
        )
    
    except Exception as e:
        logger.error(f"Error creating order: {str(e)}", exc_info=True)
        return JsonResponse(
            {"message": "Internal server error", "success": False, "error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
