from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Products, Brand, Category, Capacity
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from django.conf import settings
import logging

logger = logging.getLogger(__name__)
base_url = settings.BASE_URL

@csrf_exempt
def product_read(request):
    if request.method == 'GET':
        try:
            products = Products.objects.filter(product_status='active')
            list_data = []
            for prod in products:
                list_data.append({
                    'id': prod.id,
                    'product_name': prod.product_name,
                    'description': prod.description,
                    'product_rate': prod.product_rate,
                    'discount': prod.discount,
                    'sale_rate': prod.sale_rate,
                    'stock_qnty': prod.stock_qnty,
                    'product_status': prod.product_status,
                    'new_arrival': prod.new_arrival,
                    'most_viewed': prod.most_viewed,
                    'top_selling': prod.top_selling,
                    'discount_offer': prod.discount_offer,
                    'brand': {
                        "id": prod.brand.id,
                        "brand_name": prod.brand.brand_name
                    } if prod.brand else None,
                    'category': {
                        "id": prod.category.id,
                        "category_name": prod.category.category_name
                    } if prod.category else None, 
                    'capacity': {
                        "id": prod.capacity.id,
                        "capacity_name": prod.capacity.capacity_name
                    } if prod.capacity else None, 
                    'product_img': base_url + prod.product_img.url if prod.product_img else ""
                })
                
            return JsonResponse({"message":"Fetch Successfully","success":True,'data':list_data},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@csrf_exempt
def product_read_all(request):
    if request.method == 'GET':
        try:
            products = Products.objects.all()
            list_data = []
            for prod in products:
                list_data.append({
                    'id': prod.id,
                    'product_name': prod.product_name,
                    'description': prod.description,
                    'product_rate': prod.product_rate,
                    'discount': prod.discount,
                    'sale_rate': prod.sale_rate,
                    'stock_qnty': prod.stock_qnty,
                    'product_status': prod.product_status,
                    'new_arrival': prod.new_arrival,
                    'most_viewed': prod.most_viewed,
                    'top_selling': prod.top_selling,
                    'discount_offer': prod.discount_offer,
                    'brand': {
                        "id": prod.brand.id,
                        "brand_name": prod.brand.brand_name
                    } if prod.brand else None,
                    'category': {
                        "id": prod.category.id,
                        "category_name": prod.category.category_name
                    } if prod.category else None, 
                    'capacity': {
                        "id": prod.capacity.id,
                        "capacity_name": prod.capacity.capacity_name
                    } if prod.capacity else None, 
                    'product_img': base_url + prod.product_img.url if prod.product_img else ""
                })
                
            return JsonResponse({"message":"Fetch Successfully","success":True,'data':list_data},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)
