# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from ecomapp.models import Category
# import logging

# logger = logging.getLogger(__name__)
# base_url = 'http://127.0.0.1:8000/ecomapi'

# @csrf_exempt
# def post_category(request):
#     if request.method == 'POST':
#         try:
#             category_name = request.POST.get('category_name')
#             category_index = request.POST.get('category_index')
#             category_status = request.POST.get('category_status')
#             category_img = request.FILES.get('category_img')
            
#             if not (category_name and category_index and category_status):
#                 return JsonResponse({"message":"Please fill all the fields",'success':False},status=status.HTTP_400_BAD_REQUEST)
#             if Category.objects.filter(category_name = category_name).exists():
#                 return JsonResponse({"message":"Category already exists",'success':False},status=status.HTTP_400_BAD_REQUEST)
            
#             category_index = int(category_index)
#             category_status = category_status
            
#             cat = Category(
#                 category_name = category_name,
#                 category_index = category_index,
#                 category_status = category_status,
#                 category_img = category_img
#             )
            
#             cat.save()
#             return JsonResponse({"message":"Category created successfully","success":True},status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     else:
#         return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)
            

# @csrf_exempt
# def get_category(request):
#     if request.method == 'GET':
#         try:
#             categories = Category.objects.all()
#             categories = categories.order_by('category_index')
#             list_data = []
#             for cat in categories:
#                 list_data.append({
#                     'id':cat.id,
#                     'category_name':cat.category_name,
#                     'category_index':cat.category_index,
#                     'category_status':cat.category_status,
#                     'category_img': base_url + cat.category_img.url if cat.category_img else ""
#                 })
#             return JsonResponse({"message":"Fetch Successfully","success":True,'data':list_data},status=status.HTTP_200_OK)
#         except Exception as e:
#             return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     else:
#         return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)

# @csrf_exempt
# def update_category(request):
#     if request.method == 'POST':
#         try:
#             id = request.POST.get('id')
#             category_name = request.POST.get('category_name')
#             category_index = request.POST.get('category_index')
#             category_status = request.POST.get('category_status')
#             category_img = request.FILES.get('category_img')
            
#             if not Category.objects.filter(id = id).exists():
#                 return JsonResponse({"message":"Record not found","success":False},status=status.HTTP_400_BAD_REQUEST)
            
#             cat = Category.objects.get(id = id)
#             if category_name:
#                 cat.category_name = category_name
#             if category_index:
#                 cat.category_index = category_index
#             if category_status:
#                 cat.category_status = category_status
#             if category_img:
#                 cat.category_img = category_img
            
#             cat.save()
            
#             return JsonResponse({"message":"Update Successfully","success":True},status=status.HTTP_200_OK)
#         except Exception as e:
#             return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     else:
#         return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)

# @csrf_exempt
# def delete_category(request):
#     if request.method == 'POST':
#         try:
#             id = request.POST.get('id')
            
#             if not Category.objects.filter(id = id).exists():
#                 return JsonResponse({"message":"Record not found","success":False},status=status.HTTP_400_BAD_REQUEST)

#             cat = Category.objects.get(id = id)
#             cat.delete()
            
#             return JsonResponse({"message":"Deleted Successfully","success":True},status=status.HTTP_200_OK)
#         except Exception as e:
#             return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     else:
#         return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)



            