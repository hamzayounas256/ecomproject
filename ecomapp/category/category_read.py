from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Category
import logging

logger = logging.getLogger(__name__)
base_url = 'http://127.0.0.1:8000/ecomapi'

@csrf_exempt
def category_read(request):
    if request.method == 'GET':
        try:
            categories = Category.objects.filter(category_status='active')
            categories = categories.order_by('category_index')
            list_data = []
            for cat in categories:
                list_data.append({
                    'id':cat.id,
                    'category_name':cat.category_name,
                    'category_index':cat.category_index,
                    'category_status':cat.category_status,
                    'category_img': base_url + cat.category_img.url if cat.category_img else ""
                })
            return JsonResponse({"message":"Fetch Successfully","success":True,'data':list_data},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def category_read_all(request):
    if request.method == 'GET':
        try:
            categories = Category.objects.all()
            categories = categories.order_by('category_index')
            list_data = []
            for cat in categories:
                list_data.append({
                    'id':cat.id,
                    'category_name':cat.category_name,
                    'category_index':cat.category_index,
                    'category_status':cat.category_status,
                    'category_img': base_url + cat.category_img.url if cat.category_img else ""
                })
            return JsonResponse({"message":"Fetch Successfully","success":True,'data':list_data},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)
