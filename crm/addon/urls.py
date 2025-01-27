from django.urls import path
from .views import *
from .pdf import *
from .filter import *
from .delete import *
from .trash_item import *
urlpatterns = [
    path("add_ticket", add_ticket, name="add_ticket"),
    path("ticket_source", ticket_source, name="ticket_source"),
    path("ticket_priorities", ticket_priorities, name="ticket_priorities"),
    path("country", country, name="country"),
    path("states", states, name="states"),
    path("order_source", order_source, name="order_source"),
    
    ### add link
    path("add_ticket_form", add_ticket_form, name="add_ticket_form"),
    path("ticket_source_form", ticket_source_form, name="ticket_source_form"),
    path("ticket_priorities_form", ticket_priorities_form, name="ticket_priorities_form"),
    path("country_form", country_form, name="country_form"),
    path("states_form", states_form, name="states_form"),
    path("order_source_form", order_source_form, name="order_source_form"),
    
    
    path("ticket_stats", ticket_stats, name="ticket_stats"),
    path("ticket_stats_form", ticket_stats_form, name="ticket_stats_form"),
    path("order_status", order_status, name="order_status"),
    path("order_status_from", order_status_from, name="order_status_from"),
    
    
    path("generate_pdf_product/<id>", generate_pdf_product, name="generate_pdf_product"),
    path("generate_pdf_machine/<id>", generate_pdf_machine, name="generate_pdf_machine"),
    path("generate_pdf_order/<id>", generate_pdf_order, name="generate_pdf_order"),
    path("generate_pdf_ticket/<id>", generate_pdf_ticket, name="generate_pdf_ticket"),   
    
    
    path("ticket_list/", ticket_list, name="ticket_list"),    
    path("order_list/", order_list, name="order_list"),    
    
    ##trash
    path("delete_company/<id>", delete_company, name="delete_company"),    
    path("delete_ticket/<id>", delete_ticket, name="delete_ticket"),    
    path("delete_order/<id>", delete_order, name="delete_order"),    
    path("delete_product/<id>", delete_product, name="delete_product"),    
    path("delete_machine/<id>", delete_machine, name="delete_machine"),    
    path("delete_location/<id>", delete_location, name="delete_location"),     
    path("delete_client/<id>", delete_client, name="delete_client"),     
    
    
    ##trash Items
    path("product_trash/", product_trash, name="product_trash"),     
    path("machine_trash/", machine_trash, name="machine_trash"),     
    path("ticket_trash/", ticket_trash, name="ticket_trash"),     
    path("order_trash/", order_trash, name="order_trash"),     
    path("client_trash/", client_trash, name="client_trash"),     
    path("ratting_trash/", ratting_trash, name="ratting_trash"),     
    path("company_trash/", company_trash, name="company_trash"),     
    path("location_trash/", location_trash, name="location_trash"),     
    

]
