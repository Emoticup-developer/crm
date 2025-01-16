from django.urls import path
from .views import login_view
from .client import client_api, reset_password
from .product import product_api
from .machine import machine_api
from .company import company_api
from .location import location_api
from .tiket import ticket_api
from .order import order_api

urlpatterns = [
    path("login/", login_view, name="login"),
    path("client/", client_api, name="client_create"),
    path("client/<int:pk>/", client_api, name="client_update_delete"),
    path("client/password/<int:pk>/", reset_password, name="reset_password"),
    # product
    path("product/", product_api, name="product_api"),
    path("product/<int:pk>/", product_api, name="product_api_del"),
    # machine
    path("machine/", machine_api, name="machine_api"),
    path("machine/<int:pk>/", machine_api, name="machine_api_del"),
    # company
    path("company/", company_api, name="company"),
    path("company/<int:pk>/", company_api, name="company_del"),
    # location
    path("location/", location_api, name="location"),
    path("location/<int:pk>/", location_api, name="location_del"),
    # ticket
    path("ticket/", ticket_api, name="ticket"),
    path("ticket/<int:pk>/", ticket_api, name="ticket_del"),
    # ticket
    path("order/", order_api, name="order"),
    path("order/<int:pk>/", order_api, name="order_del"),
]
