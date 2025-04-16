from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from ecomapp.models import Users,Logout
import logging

logger=logging.getLogger(__name__)
base_url = 'http://127.0.0.1:8000/ecomapi'

@csrf_exempt
def login(request):
    if request.method != 'POST':
        return JsonResponse({"success":False,"message":"Method Not Allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        required_fields=['email','password']
        missing=[field for field in required_fields if not request.POST.get(field)]
        if missing:
            return JsonResponse({"success":False,"message":f"Missing Fields: {", ".join(missing)}"},status=status.HTTP_400_BAD_REQUEST)
        
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        try:
            user=Users.objects.get(email=email)
        except Users.DoesNotExist:
            return JsonResponse({"success":False,"message":"Email Doesn't Exists"},status=status.HTTP_400_BAD_REQUEST)
        
        if check_password(password,user.password):
            refesh_token=RefreshToken.for_user(user)
            access_token=refesh_token.access_token
            
            data={
                'name':user.name,
                'email':user.email,
                'phone_no':user.phone_no,
                'role':user.role_id.name,
                'image':'http://127.0.0.1:8000/ecomapi'+user.image.url if user.image else ""
            }
            Logout(token=access_token,user_id=user).save()
            
            return JsonResponse({"success":True,"message":"Login Successfully","access_token":str(access_token),"refresh_token":str(refesh_token),"data":data},status=status.HTTP_200_OK)
        else:
            return JsonResponse({"success":False,"message":"Wrong Credentials"},status=status.HTTP_401_UNAUTHORIZED)
        
    except Exception as e:
        return JsonResponse({"success":False,"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    