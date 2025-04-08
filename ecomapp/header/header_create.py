from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Header
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def header_create(request):
    if request.method != 'POST':
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        required_fields = ['order_date', 'order_time', 'cust_name', 'cust_address', 'cust_phone_no', 'cust_email', 'cust_nic']
        missing = [field for field in required_fields if not request.POST.get(field)]
        if missing:
            return JsonResponse({"message": f"Missing fields: {', '.join(missing)}", "success": False}, status=status.HTTP_400_BAD_REQUEST)
        
        order_date = request.POST.get('order_date')
        order_time = request.POST.get('order_time')
        cust_name = request.POST.get('cust_name')
        cust_address = request.POST.get('cust_address')
        cust_phone_no = request.POST.get('cust_phone_no')
        cust_email = request.POST.get('cust_email')
        cust_nic = request.POST.get('cust_nic')
        # total_qnty = int(request.POST.get('total_qnty',0))
        # total_amount = Decimal(request.POST.get('total_amount','0.00'))
        # total_sale_amount = Decimal(request.POST.get('total_sale_amount','0.00'))
        
        head = Header(
            order_date=order_date,
            order_time = order_time,
            cust_name = cust_name,
            cust_address=cust_address,
            cust_phone_no=cust_phone_no,
            cust_email=cust_email,
            cust_nic = cust_nic,
            # total_qnty=total_qnty,
            # total_amount=total_amount,
            # total_sale_amount=total_sale_amount
        )
        head.save()
        return JsonResponse({"message":"Record created successfully","success":True},status=status.HTTP_201_CREATED)
        
        
    except Exception as e:
        return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)






