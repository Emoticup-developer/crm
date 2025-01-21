from django.urls import path
from .views import *
from .update import *




urlpatterns = [

    path("", index, name="index"),
    path("login", login, name="login"),
    path("localization", localization, name="localization"),
    path("localization_create", localization_create, name="localization_create"),
    path("product", product, name="product"),
    path("product_create", product_create, name="product_create"),
    path("machine", machine, name="machine"),
    path("machine_create", machine_create, name="machine_create"),
    path("ticket", ticket, name="ticket"),
    path("ticket_create", ticket_create, name="ticket_create"),
    path("order", order, name="order"),
    path("create_order", create_order, name="create_order"),
    path("client", client, name="client"),
    path("client_create", client_create, name="client_create"),
    path("ratting", ratting, name="ratting"),
    
    ## All View function
    path("view_ratting/view=<id>",view_ratting,name="view_ratting"),
    path("view_client/view=<id>",view_client,name="view_client"),
    path("view_machine/view=<id>",view_machine,name="view_machine"),
    path("view_product/view=<id>",view_product,name="view_product"),
    path("view_ticket/view=<id>",view_ticket,name="view_ticket"),
    path("view_localization/view=<id>",view_localization,name="view_localization"),
    path("view_order/view=<id>",view_order,name="view_order"),
    
    ##all update
    path("order_update/update/<id>/", order_update, name="order_update"),
    path("ticket_update/update/<id>/", ticket_update, name="ticket_update"),
    path("machine_update/update/<id>/", machine_update, name="machine_update"),
    path("product_update/update/<id>/", product_update, name="product_update"),
    path("localization_update/update/<id>/", localization_update, name="localization_update"),
    path("client_update/update/<id>/", client_update, name="client_update"),

]
