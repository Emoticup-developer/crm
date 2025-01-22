from django.conf import settings
from .models import *


def shared_data(request):
    return {
        "topnavbar": TopBarIcon.objects.all(),
        "sidenavbar": SideBarIcon.objects.all(),
        "account": Client.objects.filter(username = request.user.username).first(),
    }
