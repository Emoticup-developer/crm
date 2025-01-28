from django.http import JsonResponse
from api.models import *
from .models import LogsAndHistory
from django.shortcuts import redirect


class DeviceAuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.path.startswith("/admin")
            or request.path.startswith("/api")
            or request.path.startswith("/authorize") or  request.path.startswith("/media"),
        ):
            return self.get_response(request)

        secure_key = request.COOKIES.get("secure_key")
        if secure_key and Authorize.objects.filter(key=secure_key).exists():
            return self.get_response(request)
        else:
            JsonResponse({"auth": "Failed"}, status=403)
        return JsonResponse({"error": "Unauthorized device"}, status=403)


class LogsMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.path.startswith("/admin")
            or request.path.startswith("/api")
            or request.path.startswith("/authorize") or  request.path.startswith("/media")
        ):
            return self.get_response(request)
        
        if not request.user.is_authenticated:
            return self.get_response(request)

        ip = self.get_client_ip(request)
        device = request.META.get("HTTP_USER_AGENT", "")
        method = request.method
        meta = str(request.META)
        location = request.path
        LogsAndHistory.objects.create(
            user=request.user,
            location=location,
            method=method,
            device=device,
            ip=ip,
            meta=meta,
        ).save()
        return self.get_response(request)

    @staticmethod
    def get_client_ip(request):
        """Helper method to extract client IP address."""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR", "")
        return ip
