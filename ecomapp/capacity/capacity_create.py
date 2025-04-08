from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Capacity
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def capacity_create(request):
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