from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Products, Brand, Category, Capacity
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)
base_url = 'http://127.0.0.1:8000/ecomapi'

@csrf_exempt
def product_delete(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            
            if not Products.objects.filter(id=id).exists():
                return JsonResponse({"message": "Product doesn't exists","success":False}, status=status.HTTP_400_BAD_REQUEST)
            
            prod = Products.objects.get(id=id)
            prod.delete()
            
            return JsonResponse({"message": "Record deleted successfully","success":True}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)

