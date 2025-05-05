from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Capacity
from django.db.models import Q
from django.conf import settings
import logging

logger = logging.getLogger(__name__)
base_url = settings.BASE_URL

@csrf_exempt
def capacity_read_all(request):
    if request.method == 'GET':
        try:

            capacities = Capacity.objects.all()
            
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
def capacity_read(request):
    if request.method == 'GET':
        try:

            capacities = Capacity.objects.filter(capacity_status='active')
            
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
