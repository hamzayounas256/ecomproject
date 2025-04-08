from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Detail,Header

@csrf_exempt
def detail_read(request):
    if request.method != 'GET':
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        order_num = request.GET.get('order_no')
        
        if not order_num:
            return JsonResponse({"message":"Please enter order id","success":False},status=status.HTTP_400_BAD_REQUEST)
        
        try:
            header = Header.objects.get(order_no=order_num)
        except Header.DoesNotExist:
            return JsonResponse({"message": "Order does not exist", "success": False}, status=status.HTTP_400_BAD_REQUEST)
        
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
            
        return JsonResponse({"message":"Fetch Successfully","success":True,'data':list_data,"total":{"Total Qnty":header.total_qnty,"Total Amount":float(header.total_amount),"Total Sale Amount":float(header.total_sale_amount)}},status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    