from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.contrib.auth.hashers import make_password
from ecomapp.models import Users,Roles
import logging

logger=logging.getLogger(__name__)
base_url = 'http://127.0.0.1:8000/ecomapi'

@csrf_exempt
def register(request):
    if request.method != 'POST':
        return JsonResponse({"success":False,"message":"Method Not Allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        
        required_fields=['name','email','phone_no','password','role_id']
        missing=[field for field in required_fields if not request.POST.get(field)]
        if missing:
            return JsonResponse({"success":False,"message":f"Missing Fields {(', '.join(missing))}"},status=status.HTTP_400_BAD_REQUEST)
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        password=request.POST.get('password')
        image=request.FILES.get('image')
        role_id=request.POST.get('role_id')
        
        try:
            role=Roles.objects.get(id=role_id)
        except Roles.DoesNotExist:
            return JsonResponse({"success":False,"message":"Role Doesn't Exists"},status=status.HTTP_400_BAD_REQUEST)
        
        if Users.objects.filter(email=email).exists():
            return JsonResponse({"success":False,"message":"Email Already Exists"},status=status.HTTP_400_BAD_REQUEST)
        
        user=Users.objects.create(
            name=name,
            email=email,
            phone_no=phone_no,
            password=make_password(password),
            image=image,
            role_id=role,
        )
        return JsonResponse({"success":True,"message":"Record Added Successfully"},status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return JsonResponse({"success":False,"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    