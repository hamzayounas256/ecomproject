from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Category
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def category_delete(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            
            if not Category.objects.filter(id = id).exists():
                return JsonResponse({"message":"Record not found","success":False},status=status.HTTP_400_BAD_REQUEST)

            cat = Category.objects.get(id = id)
            cat.delete()
            
            return JsonResponse({"message":"Deleted Successfully","success":True},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e),"success":False},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)
