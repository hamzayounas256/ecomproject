from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Brand
import logging

logger = logging.getLogger(__name__)
base_url = 'http://127.0.0.1:8000/ecomapi'

@csrf_exempt
def post_brand(request):
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
            

@csrf_exempt
def get_brand(request):
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

@csrf_exempt
def update_brand(request):
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

@csrf_exempt
def delete_brand(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            
            if not Brand.objects.filter(id = id).exists():
                return JsonResponse({"message":"Record not found","success":False},status=status.HTTP_400_BAD_REQUEST)

            brnd = Brand.objects.get(id = id)
            brnd.delete()
            
            return JsonResponse({"message":"Deleted Successfully","success":True},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)



            