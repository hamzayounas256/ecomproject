from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Brand
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def brand_create(request):
    if request.method == 'POST':
        try:
            brand_name = request.POST.get('brand_name')
            brand_index = request.POST.get('brand_index')
            brand_status = request.POST.get('brand_status')
            brand_img = request.FILES.get('brand_img')
            
            if not (brand_name and brand_index and brand_status):
                return JsonResponse({"message":"Please fill all the fields",'success':False},status=status.HTTP_400_BAD_REQUEST)
            if Brand.objects.filter(brand_name = brand_name).exists():
                return JsonResponse({"message":"Brand already exists",'success':False},status=status.HTTP_400_BAD_REQUEST)
            
            brand_index = int(brand_index)
            brand_status = brand_status
            
            brnd = Brand(
                brand_name = brand_name,
                brand_index = brand_index,
                brand_status = brand_status,
                brand_img = brand_img
            )
            
            brnd.save()
            return JsonResponse({"message":"Brand created successfully","success":True},status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)