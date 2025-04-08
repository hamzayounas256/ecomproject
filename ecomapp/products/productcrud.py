# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from ecomapp.models import Products, Brand, Category, Capacity
# from django.core.exceptions import ObjectDoesNotExist
# from decimal import Decimal
# import logging

# logger = logging.getLogger(__name__)
# base_url = 'http://127.0.0.1:8000/ecomapi'

# def str_to_bool(value):
#     return value.lower() == 'true' if value else False

# @csrf_exempt
# def post_product(request):
#     if request.method == 'POST':
#         try:
#             product_name = request.POST.get('product_name')
#             description = request.POST.get('description')
#             product_rate = request.POST.get('product_rate')
#             stock_qnty = request.POST.get('stock_qnty')
#             product_status = request.POST.get('product_status')
#             discount = request.POST.get('discount')
#             new_arrival = request.POST.get('new_arrival')
#             most_viewed = request.POST.get('most_viewed')
#             top_selling = request.POST.get('top_selling')
#             discount_offer = request.POST.get('discount_offer')
#             brand = request.POST.get('brand')
#             category = request.POST.get('category')
#             capacity = request.POST.get('capacity')
#             product_img = request.FILES.get('product_img')

#             if not (product_name and product_rate and stock_qnty and product_status and brand and capacity and category):
#                 return JsonResponse({"message":"Please fill all required fields", "success":False }, status = status.HTTP_400_BAD_REQUEST)

#             if Products.objects.filter(product_name=product_name).exists():
#                 return JsonResponse({"message":"Product already exists", "success":False},status=status.HTTP_400_BAD_REQUEST)
            
#             product_rate = Decimal(product_rate)
#             discount = Decimal(discount) if discount else None
#             stock_qnty = int(stock_qnty)
#             sale_rate = Decimal(product_rate-discount)
            
#             new_arrival = str_to_bool(new_arrival)
#             most_viewed = str_to_bool(most_viewed)
#             top_selling = str_to_bool(top_selling)
#             discount_offer = str_to_bool(discount_offer)
            
#             try:
#                 brand = Brand.objects.get(id=int(brand))
#             except ObjectDoesNotExist:
#                 return JsonResponse({"message": "Invalid brand ID", "success": False}, status=status.HTTP_400_BAD_REQUEST)
            
#             try:
#                 category = Category.objects.get(id=int(category))
#             except ObjectDoesNotExist:
#                 return JsonResponse({"message": "Invalid category ID", "success": False}, status=status.HTTP_400_BAD_REQUEST)
            
#             try:
#                 capacity = Capacity.objects.get(id=int(capacity))
#             except ObjectDoesNotExist:
#                 return JsonResponse({"message": "Invalid capacity ID", "success": False}, status=status.HTTP_400_BAD_REQUEST)

#             product = Products(
#                 product_name=product_name,
#                 description = description,
#                 stock_qnty = stock_qnty,
#                 product_status = product_status,
#                 product_rate = product_rate,
#                 discount = discount,
#                 sale_rate = sale_rate,
#                 new_arrival = new_arrival,
#                 most_viewed = most_viewed,
#                 top_selling = top_selling,
#                 discount_offer = discount_offer,
#                 brand = brand,
#                 category = category,
#                 capacity = capacity,
#                 product_img = product_img
#                 )
#             product.save()
#             return JsonResponse({"message": "Record created successfully","success":True}, status=status.HTTP_201_CREATED)

#         except Exception as e:
#             return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     else:
#         return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)


# @csrf_exempt
# def get_product(request):
#     if request.method == 'GET':
#         try:
#             products = Products.objects.filter(product_status='active')
#             list_data = []
#             for prod in products:
#                 list_data.append({
#                     'id': prod.id,
#                     'product_name': prod.product_name,
#                     'description': prod.description,
#                     'product_rate': prod.product_rate,
#                     'discount': prod.discount,
#                     'sale_rate': prod.sale_rate,
#                     'stock_qnty': prod.stock_qnty,
#                     'product_status': prod.product_status,
#                     'new_arrival': prod.new_arrival,
#                     'most_viewed': prod.most_viewed,
#                     'top_selling': prod.top_selling,
#                     'discount_offer': prod.discount_offer,
#                     'brand': {
#                         "id": prod.brand.id,
#                         "brand_name": prod.brand.brand_name
#                     } if prod.brand else None,
#                     'category': {
#                         "id": prod.category.id,
#                         "category_name": prod.category.category_name
#                     } if prod.category else None, 
#                     'capacity': {
#                         "id": prod.capacity.id,
#                         "capacity_name": prod.capacity.capacity_name
#                     } if prod.capacity else None, 
#                     'product_img': base_url + prod.product_img.url if prod.product_img else ""
#                 })
                
#             return JsonResponse({"message":"Fetch Successfully","success":True,'data':list_data},status=status.HTTP_200_OK)
#         except Exception as e:
#             return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     else:
#         return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
# @csrf_exempt
# def get_all_product(request):
#     if request.method == 'GET':
#         try:
#             products = Products.objects.all()
#             list_data = []
#             for prod in products:
#                 list_data.append({
#                     'id': prod.id,
#                     'product_name': prod.product_name,
#                     'description': prod.description,
#                     'product_rate': prod.product_rate,
#                     'discount': prod.discount,
#                     'sale_rate': prod.sale_rate,
#                     'stock_qnty': prod.stock_qnty,
#                     'product_status': prod.product_status,
#                     'new_arrival': prod.new_arrival,
#                     'most_viewed': prod.most_viewed,
#                     'top_selling': prod.top_selling,
#                     'discount_offer': prod.discount_offer,
#                     'brand': {
#                         "id": prod.brand.id,
#                         "brand_name": prod.brand.brand_name
#                     } if prod.brand else None,
#                     'category': {
#                         "id": prod.category.id,
#                         "category_name": prod.category.category_name
#                     } if prod.category else None, 
#                     'capacity': {
#                         "id": prod.capacity.id,
#                         "capacity_name": prod.capacity.capacity_name
#                     } if prod.capacity else None, 
#                     'product_img': base_url + prod.product_img.url if prod.product_img else ""
#                 })
                
#             return JsonResponse({"message":"Fetch Successfully","success":True,'data':list_data},status=status.HTTP_200_OK)
#         except Exception as e:
#             return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     else:
#         return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)


# @csrf_exempt
# def update_product(request):
#     if request.method == 'POST':
#         try:
#             id = request.POST.get('id')
#             product_name = request.POST.get('product_name')
#             description = request.POST.get('description')
#             product_rate = request.POST.get('product_rate')
#             stock_qnty = request.POST.get('stock_qnty')
#             product_status = request.POST.get('product_status')
#             discount = request.POST.get('discount')
#             new_arrival = request.POST.get('new_arrival')
#             most_viewed = request.POST.get('most_viewed')
#             top_selling = request.POST.get('top_selling')
#             discount_offer = request.POST.get('discount_offer')
#             brand_id = request.POST.get('brand')
#             category_id = request.POST.get('category')
#             capacity_id = request.POST.get('capacity')
#             product_img = request.FILES.get('product_img')
            
#             if not Products.objects.filter(id=id).exists():
#                 return JsonResponse({"message": "Record not found","success":False}, status=status.HTTP_400_BAD_REQUEST)
            
#             prod = Products.objects.get(id=id)
            
#             if product_name:
#                 prod.product_name = product_name
#             if description:
#                 prod.description = description
#             if product_rate:
#                 prod.product_rate = Decimal(product_rate)
#                 prod.sale_rate = Decimal(product_rate) - Decimal(discount)
#             if stock_qnty:
#                 prod.stock_qnty = int(stock_qnty)
#             if product_status:
#                 prod.product_status = product_status
#             if discount:
#                 prod.discount = Decimal(discount)
#                 prod.sale_rate = Decimal(product_rate) - Decimal(discount)
#             if new_arrival:
#                 prod.new_arrival = str_to_bool(new_arrival)
#             if most_viewed:
#                 prod.most_viewed = str_to_bool(most_viewed)
#             if top_selling:
#                 prod.top_selling = str_to_bool(top_selling)
#             if discount_offer:
#                 prod.discount_offer = str_to_bool(discount_offer)
#             try:
#                 if brand_id:
#                     prod.brand = Brand.objects.get(id=int(brand_id))
#                 if category_id:
#                     prod.category = Category.objects.get(id=int(category_id))
#                 if capacity_id:
#                     prod.capacity = Capacity.objects.get(id=int(capacity_id))
#             except ObjectDoesNotExist:
#                 return JsonResponse({"message": "Invalid brand, category, or capacity ID", "success": False}, status=status.HTTP_400_BAD_REQUEST)
#             if product_img:
#                 prod.product_img = product_img
                
#             prod.save()
            
#             return JsonResponse({"message": "Record updated successfully","success":True}, status=status.HTTP_201_CREATED)

#         except Exception as e:
#             return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     else:
#         return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)

# @csrf_exempt
# def delete_product(request):
#     if request.method == 'POST':
#         try:
#             id = request.POST.get('id')
            
#             if not Products.objects.filter(id=id).exists():
#                 return JsonResponse({"message": "Product doesn't exists","success":False}, status=status.HTTP_400_BAD_REQUEST)
            
#             prod = Products.objects.get(id=id)
#             prod.delete()
            
#             return JsonResponse({"message": "Record deleted successfully","success":True}, status=status.HTTP_201_CREATED)

#         except Exception as e:
#             return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     else:
#         return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)



