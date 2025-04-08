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
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    try:
        # required_fields = ['order_no','order_date','order_time','cust_name','cust_address','cust_phone_no','cust_email','cust_nic']
        # missing = [field for field in required_fields if not required_fields.GET.get(field)]
        # if missing:
        #     return JsonResponse({"message":f"Missing fields: {', '.join(missing)}","success":False},status=status.HTTP_400_BAD_REQUEST)
        
        order_no = request.GET.get('order_no')
        # order_date = request.GET.get('order_date')
        # order_time = request.GET.get('order_time')
        # cust_name = request.GET.get('cust_name')
        # cust_address = request.GET.get('cust_address')
        # cust_phone = request.GET.get('cust_phone')
        # cust_email = request.GET.get('cust_email')
        # cust_nic = request.GET.get('cust_nic')
        
        try:
            header = Header.objects.get(order_no=order_no)
        except Header.DoesNotExist:
            return JsonResponse({"message": "Order does not exist", "success": False}, status=status.HTTP_400_BAD_REQUEST)
        
        data = {
            'order_date': header.order_date,
            'order_time': header.order_time,
            'cust_name': header.cust_name,
            'cust_address': header.cust_address,
            'cust_phone_no': header.cust_phone_no,
            'cust_email': header.cust_email,
            'cust_nic': header.cust_nic,
            'order_status':header.order_status,
            'total_qnty': header.total_qnty,
            'total_amount': float(header.total_amount),
            'total_sale_amount': float(header.total_sale_amount)
        }
        
        details = Detail.objects.filter(order_no=header)
        
        list_data = []
        for det in details:
            list_data.append({
                'id':det.id,
                'product_name':det.product_name,
                'product_qnty':det.product_qnty,
                'product_rate':det.product_rate,
                'product_amount':det.product_amount,
                'product_sale_rate':det.product_sale_rate,
                'product_sale_amount':det.product_sale_amount,
            })
        
        return JsonResponse({"message":"Fetch Successfully","success":True,'header':data,'detail':list_data},status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    