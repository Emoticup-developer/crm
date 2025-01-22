from django.urls import path
from .views import *
from .update import *
from .csv import *


urlpatterns = [

    path("", index, name="index"),
    path("login", login_user, name="login"),
    path("user_logout", user_logout, name="user_logout"),
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
    path("company", company, name="company"),
    path("company_create", company_create, name="company_create"),
    path("location", location, name="location"),
    path("location_create", location_create, name="location_create"),
    path("ratting", ratting, name="ratting"),
    
    ## All View function
    path("view_ratting/view=<id>",view_ratting,name="view_ratting"),
    path("view_client/view=<id>",view_client,name="view_client"),
    path("view_machine/view=<id>",view_machine,name="view_machine"),
    path("view_product/view=<id>",view_product,name="view_product"),
    path("view_ticket/view=<id>",view_ticket,name="view_ticket"),
    path("view_localization/view=<id>",view_localization,name="view_localization"),
    path("view_order/view=<id>",view_order,name="view_order"),
    path("view_company/view=<id>",view_company,name="view_company"),
    path("view_location/view=<id>",view_location,name="view_location"),
    
    ##all update
    path("order_update/update/<id>/", order_update, name="order_update"),
    path("ticket_update/update/<id>/", ticket_update, name="ticket_update"),
    path("machine_update/update/<id>/", machine_update, name="machine_update"),
    path("product_update/update/<id>/", product_update, name="product_update"),
    path("localization_update/update/<id>/", localization_update, name="localization_update"),
    path("client_update/update/<id>/", client_update, name="client_update"),
    path("client_company/update/<id>/", client_company, name="client_company"),
    path("client_location/update/<id>/", client_location, name="client_location"),
    
    
    ### download csv
    
    path("download_localization/download/csv/",download_localization , name="download_localization"),
    path("download_client/update/download/csv/", download_client, name="download_client"),
    path("download_machine/update/download/csv/", download_machine, name="download_machine"),
    path("download_order/update/download/csv/", download_order, name="download_order"),
    path("download_ticket/update/download/csv/", download_ticket, name="download_ticket"),
    path("download_ratting/update/download/csv/", download_ratting, name="download_ratting"),
    path("download_product/update/download/csv/", download_product, name="download_product"),
        path("download_company/update/download/csv/", download_company, name="download_company"),
    path("download_location/update/download/csv/", download_location, name="download_location"),
    

]
