from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Capacity
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)
base_url = 'http://127.0.0.1:8000/ecomapi'

@csrf_exempt
def post_capacity(request):
    if request.method == 'POST':
        try:
            capacity_name = request.POST.get('capacity_name')
            capacity_index = request.POST.get('capacity_index')
            capacity_status = request.POST.get('capacity_status')
            capacity_img = request.FILES.get('capacity_img')
            
            if not (capacity_name and capacity_index and capacity_status):
                return JsonResponse({"message":"Please fill all the fields",'success':False},status=status.HTTP_400_BAD_REQUEST)
            if Capacity.objects.filter(capacity_name = capacity_name).exists():
                return JsonResponse({"message":"Capacity already exists",'success':False},status=status.HTTP_400_BAD_REQUEST)
            
            capacity_index = int(capacity_index)
            capacity_status = capacity_status
            
            cap = Capacity(
                capacity_name = capacity_name,
                capacity_index = capacity_index,
                capacity_status = capacity_status,
                capacity_img = capacity_img
            )
            
            cap.save()
            return JsonResponse({"message":"Capacity created successfully","success":True},status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)
            

@csrf_exempt
def get_capacity(request):
    if request.method == 'GET':
        try:

            capacities = Capacity.objects.all()
            
            # search = request.GET.get('search', '')
            # if search:
            #     capacities = capacities.filter(
            #         Q(capacity_name__icontains = search)
            #     )
                
            capacities = capacities.order_by('capacity_index')
            
            list_data = []
            for cap in capacities:
                list_data.append({
                    'id':cap.id,
                    'capacity_name':cap.capacity_name,
                    'capacity_index':cap.capacity_index,
                    'capacity_status':cap.capacity_status,
                    'capacity_img': base_url + cap.capacity_img.url if cap.capacity_img else ""
                })
            return JsonResponse({"message":"Fetch Successfully","success":True,'data':list_data},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def update_capacity(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            capacity_name = request.POST.get('capacity_name')
            capacity_index = request.POST.get('capacity_index')
            capacity_status = request.POST.get('capacity_status')
            capacity_img = request.FILES.get('capacity_img')
            
            if not Capacity.objects.filter(id = id).exists():
                return JsonResponse({"message":"Record not found","success":False},status=status.HTTP_400_BAD_REQUEST)
            
            cap = Capacity.objects.get(id = id)
            if capacity_name:
                cap.capacity_name = capacity_name
            if capacity_index:
                cap.capacity_index = capacity_index
            if capacity_status:
                cap.capacity_status = capacity_status
            if capacity_img:
                cap.capacity_img = capacity_img
            
            cap.save()
            
            return JsonResponse({"message":"Update Successfully","success":True},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def delete_capacity(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            
            if not Capacity.objects.filter(id = id).exists():
                return JsonResponse({"message":"Record not found","success":False},status=status.HTTP_400_BAD_REQUEST)

            cap = Capacity.objects.get(id = id)
            cap.delete()
            
            return JsonResponse({"message":"Deleted Successfully","success":True},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)



            