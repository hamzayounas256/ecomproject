from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from ecomapp.models import Users,Logout

@csrf_exempt
def logout(request):
    if request.method != 'POST':
        return JsonResponse({"success":False,"message":"Method Not Allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        id=request.POST.get('id')
        
        try:
            user=Users.objects.get(id=id)
        except Users.DoesNotExist:
            return JsonResponse({"success":False,"message":"User Does Not Exists"},status=status.HTTP_400_BAD_REQUEST)
            
        logout = Logout.objects.filter(user_id=user)
        logout.delete()
        return JsonResponse({"success":True,"message":"Logout Successfully"},status=status.HTTP_200_OK)
        
    except Exception as e:
        return JsonResponse({"success":False, "error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    