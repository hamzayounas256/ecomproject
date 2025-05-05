from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Brand
from django.conf import settings
import logging

logger = logging.getLogger(__name__)
base_url = settings.BASE_URL

@csrf_exempt
def brand_read(request):
    if request.method == 'GET':
        try:
            brands = Brand.objects.filter(brand_status='active')
            brands = brands.order_by('brand_index')
            list_data = []
            for brnd in brands:
                list_data.append({
                    'id':brnd.id,
                    'brand_name':brnd.brand_name,
                    'brand_index':brnd.brand_index,
                    'brand_status':brnd.brand_status,
                    'brand_img': base_url + brnd.brand_img.url if brnd.brand_img else ""
                })
            return JsonResponse({"message":"Fetch Successfully","success":True,'data':list_data},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@csrf_exempt
def brand_read_all(request):
    if request.method == 'GET':
        try:
            brands = Brand.objects.all()
            brands = brands.order_by('brand_index')
            list_data = []
            for brnd in brands:
                list_data.append({
                    'id':brnd.id,
                    'brand_name':brnd.brand_name,
                    'brand_index':brnd.brand_index,
                    'brand_status':brnd.brand_status,
                    'brand_img': base_url + brnd.brand_img.url if brnd.brand_img else ""
                })
            return JsonResponse({"message":"Fetch Successfully","success":True,'data':list_data},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)