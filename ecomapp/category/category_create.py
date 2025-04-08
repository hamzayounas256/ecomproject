from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Category
import logging

logger = logging.getLogger(__name__)
base_url = 'http://127.0.0.1:8000/ecomapi'

@csrf_exempt
def category_create(request):
    if request.method == 'POST':
        try:
            category_name = request.POST.get('category_name')
            category_index = request.POST.get('category_index')
            category_status = request.POST.get('category_status')
            category_img = request.FILES.get('category_img')
            
            if not (category_name and category_index and category_status):
                return JsonResponse({"message":"Please fill all the fields",'success':False},status=status.HTTP_400_BAD_REQUEST)
            if Category.objects.filter(category_name = category_name).exists():
                return JsonResponse({"message":"Category already exists",'success':False},status=status.HTTP_400_BAD_REQUEST)
            
            category_index = int(category_index)
            category_status = category_status
            
            cat = Category(
                category_name = category_name,
                category_index = category_index,
                category_status = category_status,
                category_img = category_img
            )
            
            cat.save()
            return JsonResponse({"message":"Category created successfully","success":True},status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)