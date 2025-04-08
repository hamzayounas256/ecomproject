from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Capacity
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def capacity_update(request):
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
