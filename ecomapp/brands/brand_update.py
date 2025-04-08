from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Brand
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def brand_update(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            brand_name = request.POST.get('brand_name')
            brand_index = request.POST.get('brand_index')
            brand_status = request.POST.get('brand_status')
            brand_img = request.FILES.get('brand_img')
            
            if not Brand.objects.filter(id = id).exists():
                return JsonResponse({"message":"Record not found","success":False},status=status.HTTP_400_BAD_REQUEST)
            
            brnd = Brand.objects.get(id = id)
            if brand_name:
                brnd.brand_name = brand_name
            if brand_index:
                brnd.brand_index = brand_index
            if brand_status:
                brnd.brand_status = brand_status
            if brand_img:
                brnd.brand_img = brand_img
            
            brnd.save()
            
            return JsonResponse({"message":"Update Successfully","success":True},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)