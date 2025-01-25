from django.urls import path
from .views import *



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
    
]
