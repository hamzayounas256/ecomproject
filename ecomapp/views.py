# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from .models import Capacity
# from .serializers import CapacitySerializer

# @api_view(['GET'])
# def get_brand(request):
#     try:
#         brands = Brand.objects.all()
#         if not brands.exists():
#             return Response({"success":False,"message": "No brands found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = BrandSerializer(brands, many=True)
#         return Response({"success":True,"data":serializer.data}, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({"success":False,"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['POST'])
# def post_brand(request):
#     serializer = BrandSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(
#             {"success":True, "message": "Brand created successfully", "data": serializer.data}, 
#             status=status.HTTP_201_CREATED
#         )
#     return Response({"success":False,"error": "Invalid data", "details": serializer.errors}, 
#                     status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT', 'DELETE'])
# def update_brand(request, pk):
#     try:
#         brand = Brand.objects.get(pk=pk)
#     except Brand.DoesNotExist:
#         return Response({"success":False,"message": "Brand not found"}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = BrandSerializer(brand, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success":True,"message": "Brand updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response({"success":False,"message": "Invalid data", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         brand.delete()
#         return Response({"success":True,"message": "Brand deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def get_category(request):
#     try:
#         categories = Category.objects.all()
#         if not categories.exists():
#             return Response({"success":False,"message": "No categories found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = CategorySerializer(categories, many=True)
#         return Response({"success":True,"data":serializer.data}, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({"success":False,"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# @api_view(['POST'])
# def post_category(request):
#     serializer = CategorySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(
#             {"success":True,"message": "Category created successfully", "data": serializer.data}, 
#             status=status.HTTP_201_CREATED
#         )
#     return Response({"success":False,"error": "Invalid data", "details": serializer.errors}, 
#                     status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['PUT', 'DELETE'])
# def update_category(request, pk):
#     try:
#         categories = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         return Response({"success":False,"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = CategorySerializer(categories, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success":True,"message": "Category updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response({"success":False,"message": "Invalid data", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         categories.delete()
#         return Response({"success":True,"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET'])
# def get_capacity(request):
#     try:
#         capacities = Capacity.objects.all()
#         if not capacities.exists():
#             return Response({"success":False,"message": "No capacities found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = CapacitySerializer(capacities, many=True)
#         return Response({"success":True,"data":serializer.data}, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({"success":False, "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['POST'])
# def post_capacity(request):
#     serializer = CapacitySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(
#             {"success":True,"message": "Capacity created successfully", "data": serializer.data}, 
#             status=status.HTTP_201_CREATED
#         )
#     return Response({"success":False,"error": "Invalid data", "details": serializer.errors}, 
#                     status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['PUT', 'DELETE'])
# def update_capacity(request, pk):
#     try:
#         capacities = Capacity.objects.get(pk=pk)
#     except Capacity.DoesNotExist:
#         return Response({"success":False,"message": "Capacity not found"}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = CapacitySerializer(capacities, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success":True,"message": "Capacity updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response({"success":False,"message": "Invalid data", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         capacities.delete()
#         return Response({"success":True, "message": "Capacity deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET'])
# def get_product(request):
#     try:
#         products = Product.objects.all()
#         if not products.exists():
#             return Response({"success":False, "message": "No products found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ProductSerializer(products, many=True)
#         return Response({"success":True,"data":serializer.data}, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# @api_view(['POST'])
# def post_product(request):
#     serializer = ProductSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(
#             {"success":True,"message":"Product created successfully", "data": serializer.data
#         }, status=status.HTTP_201_CREATED
#         )
#     return Response({
#         "success":False,"error":"Invalid Data","details":serializer.errors
#     }, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['PUT', 'DELETE'])
# def update_product(request, pk):
#     try:
#         products = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response({"success":False,"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = ProductSerializer(products, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success":True,"message": "Product updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response({"success":False,"message": "Invalid data", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         products.delete()
#         return Response({"success":True, "message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    
    
    