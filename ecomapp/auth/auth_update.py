from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.contrib.auth.hashers import make_password
from ecomapp.models import Users,Roles

import logging

logger=logging.getLogger(__name__)

@csrf_exempt
def auth_update(request):
    if request.method != 'POST':
        return JsonResponse({"success":False,"message":"method not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        id=request.POST.get('id')
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        password=request.POST.get('password')
        role=request.POST.get('role_id')
        image=request.FILES.get('image')
        
        
        if not Users.objects.filter(id=id).exists():
            return JsonResponse({"success":False,"message":"User Doesn't Exists"},status=status.HTTP_404_NOT_FOUND)
        
        try:
            role=Roles.objects.get(id=role)
        except Roles.DoesNotExist:
            return JsonResponse({"success":False,"message":"Role Doesn't Exists"},status=status.HTTP_404_NOT_FOUND)
        
        if Users.objects.filter(email=email).exists():
            return JsonResponse({"success":False,"message":"Email Already Taken"},status=status.HTTP_226_IM_USED)
        
        update=Users.objects.get(id=id)
        if name:
            update.name=name
        if email:
            update.email=email
        if password:
            update.password=make_password(password)
        if phone_no:
            update.phone_no=phone_no
        if role:
            update.role_id=role
        if image:
            update.image=image
        
        update.save()
        return JsonResponse({"success":True,"message":"Record Updated Successfully"},status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return JsonResponse({"success":False,"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)