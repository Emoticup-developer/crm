from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from django.utils import timezone
from .models import *
from .forms import *


def generate_tokens(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


@api_view(["POST"])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        tokens = generate_tokens(user)
        return Response(
            {"message": "Login successful", "tokens": tokens, "role": user.is_staff},
            status=200,
        )
    else:
        return Response({"error": "Invalid credentials"}, status=401)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def create_customer(request):

    return Response({"message": f"Welcome, {request.user.username}!"}, status=200)


def model_counts(request):
    today = timezone.now()
    models = [Client, Product, Machine, Company, Location, Ticket, Order, Localization]

    result = {"day": {}, "month": {}, "year": {}}

    for model in models:
        result["day"][model.__name__] = model.objects.filter(
            created_at__date=today.date()
        ).count()
        result["month"][model.__name__] = model.objects.filter(
            created_at__month=today.month, created_at__year=today.year
        ).count()
        result["year"][model.__name__] = model.objects.filter(
            created_at__year=today.year
        ).count()

    # Wrap the result in a list
    return JsonResponse([result], safe=False)


@api_view(["GET"])
def ticket_meta(request):
    office = list(Company.objects.filter(associated_employee=Client.objects.get(username=request.user.username)).values("id", "company_name")) if Client.objects.filter(username=request.user.username).exists() else []
    data = {
        "products": list(Product.objects.values("id", "product_code")),
        "office":office,
        "machines": list(Machine.objects.values("id", "machine_id")),
        "ticket_types": list(TicketType.objects.values("id", "name")),
        "ticket_sources": list(TicketSource.objects.values("id", "name")),
        "ticket_priorities": list(
            TicketPriority.objects.values("id", "name", "description")
        ),
        "companies": list(Company.objects.values("id", "company_name")),
    }

    return JsonResponse([data], safe=False)
