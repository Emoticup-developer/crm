
from django.http import JsonResponse
from api.models import *

class DeviceAuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin') or request.path.startswith('/authorize'):
            return self.get_response(request)
        
        secure_key = request.COOKIES.get('secure_key')
        if secure_key and Authorize.objects.filter(key=secure_key).exists():
            return self.get_response(request)
        else:
            JsonResponse({"auth":"Failed"}, status=403) 
        return JsonResponse({'error': 'Unauthorized device'}, status=403)
