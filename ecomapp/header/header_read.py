from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Header, Detail
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def header_read(request):
    if request.method != 'GET':
        return JsonResponse({"message": "Method not allowed", "success": False}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        order_no = request.GET.get('order_no')
        cust_email = request.GET.get('cust_email')

        # If order_no is provided, fetch specific order
        if order_no:
            try:
                if cust_email:
                    header = Header.objects.get(order_no=order_no, cust_email=cust_email)
                else:
                    header = Header.objects.get(order_no=order_no)
            except Header.DoesNotExist:
                return JsonResponse({"message": "Order not found", "success": False}, status=status.HTTP_400_BAD_REQUEST)

            data = {
                'order_date': header.order_date,
                'order_time': header.order_time,
                'cust_name': header.cust_name,
                'cust_address': header.cust_address,
                'cust_phone_no': header.cust_phone_no,
                'cust_email': header.cust_email,
                'cust_nic': header.cust_nic,
                'order_status': header.order_status,
                'total_qnty': header.total_qnty,
                'total_amount': float(header.total_amount),
                'total_sale_amount': float(header.total_sale_amount)
            }

            details = Detail.objects.filter(order_no=header)
            list_data = [{
                'id': det.id,
                'product_name': det.product_name,
                'product_qnty': det.product_qnty,
                'product_rate': det.product_rate,
                'product_amount': det.product_amount,
                'product_sale_rate': det.product_sale_rate,
                'product_sale_amount': det.product_sale_amount,
                'product_img':"http://127.0.0.1:8000/ecomapi"+det.product_img.url if det.product_img else "",
            } for det in details]

            return JsonResponse({"message": "Fetch Successfully", "success": True, 'header': data, 'detail': list_data}, status=status.HTTP_200_OK)

        else:
            # If order_no is not provided, fetch all orders
            headers = Header.objects.all()
            all_data = []

            for header in headers:
                header_data = {
                    'order_no': header.order_no,
                    'order_date': header.order_date,
                    'order_time': header.order_time,
                    'cust_name': header.cust_name,
                    'cust_address': header.cust_address,
                    'cust_phone_no': header.cust_phone_no,
                    'cust_email': header.cust_email,
                    'cust_nic': header.cust_nic,
                    'order_status': header.order_status,
                    'total_qnty': header.total_qnty,
                    'total_amount': float(header.total_amount),
                    'total_sale_amount': float(header.total_sale_amount)
                }

                details = Detail.objects.filter(order_no=header)
                detail_list = [{
                    'id': det.id,
                    'product_name': det.product_name,
                    'product_qnty': det.product_qnty,
                    'product_rate': det.product_rate,
                    'product_amount': det.product_amount,
                    'product_sale_rate': det.product_sale_rate,
                    'product_sale_amount': det.product_sale_amount,
                } for det in details]

                all_data.append({
                    'header': header_data,
                    'detail': detail_list
                })

            return JsonResponse({"message": "All Orders Fetched Successfully", "success": True, 'orders': all_data}, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error("Error in header_read: %s", str(e))
        return JsonResponse({"message": "Error", "error": str(e), "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
