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
def product_update(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
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
            brand_id = request.POST.get('brand')
            category_id = request.POST.get('category')
            capacity_id = request.POST.get('capacity')
            product_img = request.FILES.get('product_img')
            
            if not Products.objects.filter(id=id).exists():
                return JsonResponse({"message": "Record not found","success":False}, status=status.HTTP_400_BAD_REQUEST)
            
            prod = Products.objects.get(id=id)
            
            if product_name:
                prod.product_name = product_name
            if description:
                prod.description = description
            if product_rate:
                prod.product_rate = Decimal(product_rate)
                prod.sale_rate = Decimal(product_rate) - Decimal(discount)
            if stock_qnty:
                prod.stock_qnty = int(stock_qnty)
            if product_status:
                prod.product_status = product_status
            if discount:
                prod.discount = Decimal(discount)
                prod.sale_rate = Decimal(product_rate) - Decimal(discount)
            if new_arrival:
                prod.new_arrival = str_to_bool(new_arrival)
            if most_viewed:
                prod.most_viewed = str_to_bool(most_viewed)
            if top_selling:
                prod.top_selling = str_to_bool(top_selling)
            if discount_offer:
                prod.discount_offer = str_to_bool(discount_offer)
            try:
                if brand_id:
                    prod.brand = Brand.objects.get(id=int(brand_id))
                if category_id:
                    prod.category = Category.objects.get(id=int(category_id))
                if capacity_id:
                    prod.capacity = Capacity.objects.get(id=int(capacity_id))
            except ObjectDoesNotExist:
                return JsonResponse({"message": "Invalid brand, category, or capacity ID", "success": False}, status=status.HTTP_400_BAD_REQUEST)
            if product_img:
                prod.product_img = product_img
                
            prod.save()
            
            return JsonResponse({"message": "Record updated successfully","success":True}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)