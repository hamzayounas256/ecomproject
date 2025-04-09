from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Detail, Header, Products
from decimal import Decimal

import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def detail_create(request):
    if request.method != 'POST':
        return JsonResponse({"message": "Method not allowed", "success": False}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    try:
        required_fields = ['order_no','product_code','product_qnty']
        missing = [field for field in required_fields if not request.POST.get(field)]
        if missing:
            return JsonResponse({"message": f"Missing fields: {', '.join(missing)}", "success": False}, status=status.HTTP_400_BAD_REQUEST)

        order_no = int(request.POST.get('order_no','0'))
        product_code = int(request.POST.get('product_code','0'))
        product_qnty = int(request.POST.get('product_qnty','0'))
        # product_name = request.POST.get('product_name')
        # product_rate = Decimal(request.POST.get('product_rate','0.00'))
        # product_sale_rate = Decimal(request.POST.get('product_sale_rate','0.00'))
        # product_amount = Decimal(request.POST.get('product_amount','0.00'))
        # product_sale_amount = Decimal(request.POST.get('product_sale_amount','0.00'))
        

        try:
            order_no = Header.objects.get(order_no=order_no)
        except Header.DoesNotExist:
            return JsonResponse({"message": "Invalid order number", "success": False}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Products.objects.get(id=product_code)
        except Products.DoesNotExist:
            return JsonResponse({"message": "Invalid product", "success": False}, status=status.HTTP_400_BAD_REQUEST)

        discount = product.discount or Decimal('0.00')
        product_name = product.product_name
        product_rate = product.product_rate

        product_amount = product_rate * product_qnty
        product_sale_rate = product_rate - discount
        product_sale_amount = product_sale_rate * product_qnty

        detail = Detail.objects.create(
            order_no=order_no,
            product_code=product,
            product_name=product_name,
            product_rate=product_rate,
            product_qnty=product_qnty,
            product_amount=product_amount,
            product_sale_rate=product_sale_rate,
            product_sale_amount=product_sale_amount
        )
        
        # 🔄 Recalculate Header totals
        details = Detail.objects.filter(order_no=order_no)
        total_qnty = sum([d.product_qnty for d in details])
        total_amount = sum([d.product_amount for d in details])
        total_sale_amount = sum([d.product_sale_amount for d in details])

        order_no.total_qnty = total_qnty
        order_no.total_amount = total_amount
        order_no.total_sale_amount = total_sale_amount
        order_no.save()
        
        # detail.save()
        return JsonResponse({
            "message": "Record created successfully",
            "success": True,
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return JsonResponse({"message": "Error", "success": False, "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

