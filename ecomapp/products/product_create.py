from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Products, Brand, Category, Capacity
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

def str_to_bool(value):
    return value.lower() == 'true' if value else False

@csrf_exempt
def product_create(request):
    if request.method == 'POST':
        try:
            product_name = request.POST.get('product_name')
            description = request.POST.get('description')
            product_rate = request.POST.get('product_rate')
            stock_qnty = request.POST.get('stock_qnty')
            product_status = request.POST.get('product_status')
            discount = request.POST.get('discount')
            new_arrival = request.POST.get('new_arrival')
            most_viewed = request.POST.get('most_viewed')
            top_selling = request.POST.get('top_selling')
            discount_offer = request.POST.get('discount_offer')
            brand = request.POST.get('brand')
            category = request.POST.get('category')
            capacity = request.POST.get('capacity')
            product_img = request.FILES.get('product_img')

            if not (product_name and product_rate and stock_qnty and product_status and brand and capacity and category):
                return JsonResponse({"message":"Please fill all required fields", "success":False }, status = status.HTTP_400_BAD_REQUEST)

            if Products.objects.filter(product_name=product_name).exists():
                return JsonResponse({"message":"Product already exists", "success":False},status=status.HTTP_400_BAD_REQUEST)
            
            product_rate = Decimal(product_rate)
            discount = Decimal(discount) if discount else 0.00
            stock_qnty = int(stock_qnty)
            sale_rate = Decimal(product_rate-discount)
            
            new_arrival = str_to_bool(new_arrival)
            most_viewed = str_to_bool(most_viewed)
            top_selling = str_to_bool(top_selling)
            discount_offer = str_to_bool(discount_offer)
            
            try:
                brand = Brand.objects.get(id=int(brand))
            except ObjectDoesNotExist:
                return JsonResponse({"message": "Invalid brand ID", "success": False}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                category = Category.objects.get(id=int(category))
            except ObjectDoesNotExist:
                return JsonResponse({"message": "Invalid category ID", "success": False}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                capacity = Capacity.objects.get(id=int(capacity))
            except ObjectDoesNotExist:
                return JsonResponse({"message": "Invalid capacity ID", "success": False}, status=status.HTTP_400_BAD_REQUEST)

            product = Products(
                product_name=product_name,
                description = description,
                stock_qnty = stock_qnty,
                product_status = product_status,
                product_rate = product_rate,
                discount = discount,
                sale_rate = sale_rate,
                new_arrival = new_arrival,
                most_viewed = most_viewed,
                top_selling = top_selling,
                discount_offer = discount_offer,
                brand = brand,
                category = category,
                capacity = capacity,
                product_img = product_img
                )
            product.save()
            return JsonResponse({"message": "Record created successfully","success":True}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)