from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.contrib.auth.hashers import make_password
from ecomapp.models import Users,Roles,OTP
from django.core.mail import send_mail
from django.conf import settings
from ecomproject.settings import set_email_config
import logging,random

logger=logging.getLogger(__name__)
base_url = 'http://127.0.0.1:8000/ecomapi'

def generate_otp():
    otp=int(''.join(random.sample('0123456789',4)))
    return otp

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
        otp=generate_otp()
        otp_instance=OTP(otp=otp)
        otp_instance.save()
        send_register_email(email,otp,name)
        return JsonResponse({"message":"OTP Sent Successfully","success":True},status=status.HTTP_200_OK)
        # user=Users.objects.create(
        #     name=name,
        #     email=email,
        #     phone_no=phone_no,
        #     password=make_password(password),
        #     image=image,
        #     role_id=role,
        # )
        # return JsonResponse({"success":True,"message":"Record Added Successfully"},status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return JsonResponse({"success":False,"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@csrf_exempt
def verify_otp(request):
    if request.method=='POST':
        try:
            otp=request.POST.get('otp')
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone_no=request.POST.get('phone_no')
            password=request.POST.get('password')
            image=request.FILES.get('image')
            role_id=request.POST.get('role_id')
            
            if not otp:
                return JsonResponse({"message":"Required OTP","success":False},status=status.HTTP_400_BAD_REQUEST)
            if not OTP.objects.filter(otp=otp).exists():
                return JsonResponse({"message":"Your OTP is expired","success":False},status=status.HTTP_401_UNAUTHORIZED)
            if OTP.objects.get(otp=otp):
                user=Users.objects.create(
                    name=name,
                    email=email,
                    phone_no=phone_no,
                    password=make_password(password),
                    image=image,
                    role_id=Roles.objects.get(id=role_id),
                )
                return JsonResponse({"success":True,"message":"Record Added Successfully"},status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@csrf_exempt
def resend_otp(request):
    if request.method=='POST':
        try:
            email=request.POST.get('email')
            name=request.POST.get('name')
            otp=generate_otp()
            if otp:
                send_register_email(email,otp,name)
                return JsonResponse({"message":"OTP send Successfully","success":True},status=status.HTTP_200_OK)
            return JsonResponse({"message":"Error in OTP generated","success":False},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"message":"Error","error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({"message":"Method not allowed","success":False},status=status.HTTP_405_METHOD_NOT_ALLOWED)


def send_register_email(email, otp, name):
    email_setting = set_email_config(primary=True)
    settings.EMAIL_HOST_USER = email_setting["EMAIL_HOST_USER"]
    settings.EMAIL_HOST_PASSWORD = email_setting["EMAIL_HOST_PASSWORD"]
    print(settings.EMAIL_HOST_USER)
    print(settings.EMAIL_HOST_PASSWORD)
    
    subject = "Billilo - New Account Registration"
    message = f"""Dear {name},

Please use the One-Time Password (OTP) below to proceed with account registration.

Your OTP: {otp}

This OTP is valid for the next 5 minutes. If you did not request a password reset, please ignore this email or contact our support team immediately.

For security reasons, please do not share this OTP with anyone.

Regards,
Billilo"""
    
    email_form = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_form, recipient_list)
    return True
