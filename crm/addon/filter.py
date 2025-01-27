import django_filters
from api.models import *


class TicketFilter(django_filters.FilterSet):
    ticket_id = django_filters.CharFilter(lookup_expr="icontains", label="Ticket ID")
    type = django_filters.ModelChoiceFilter(
        queryset=TicketType.objects.all(), label="Type"
    )
    source = django_filters.ModelChoiceFilter(
        queryset=TicketSource.objects.all(), label="Source"
    )
    priority = django_filters.ModelChoiceFilter(
        queryset=TicketPriority.objects.all(), label="Priority"
    )
    status = django_filters.ModelChoiceFilter(
        queryset=TicketStatus.objects.all(), label="Status"
    )
    created_at = django_filters.DateFromToRangeFilter(label="Created Between")
    updated_at = django_filters.DateFromToRangeFilter(label="Updated Between")

    class Meta:
        model = Ticket
        fields = [
            "ticket_id",
            "type",
            "source",
            "priority",
            "status",
            "created_at",
            "updated_at",
        ]


class OrderFilter(django_filters.FilterSet):
    order_id = django_filters.CharFilter(lookup_expr="icontains", label="Order ID")
    po_number = django_filters.CharFilter(lookup_expr="icontains", label="PO Number")
    dc_number = django_filters.CharFilter(lookup_expr="icontains", label="DC Number")
    client = django_filters.ModelChoiceFilter(
        queryset=Client.objects.all(), label="Client"
    )
    source = django_filters.ModelChoiceFilter(
        queryset=OrderSource.objects.all(), label="Order Source"
    )
    machine = django_filters.ModelChoiceFilter(
        queryset=Machine.objects.all(), label="Machine"
    )
    status = django_filters.ModelChoiceFilter(
        queryset=OrderStatus.objects.all(), label="Status"
    )
    order_date = django_filters.DateFromToRangeFilter(label="Order Date")
    created_at = django_filters.DateFromToRangeFilter(label="Created At")
    updated_at = django_filters.DateFromToRangeFilter(label="Updated At")

    class Meta:
        model = Order
        fields = [
            "order_id",
            "po_number",
            "dc_number",
            "client",
            "source",
            "machine",
            "status",
            "order_date",
            "created_at",
            "updated_at",
        ]









from django.shortcuts import render
from api.models import *
from .form import *


def ticket_list(request):
    filter_set = TicketFilter(request.GET, queryset=Ticket.objects.filter(trash = False).all())
    tickets = filter_set.qs 
    return render(request, "webapp/ticket.html", {"filter": filter_set, "ticket": tickets})


def order_list(request):
    filter_set = OrderFilter(request.GET, queryset=Order.objects.filter(trash = False).all())
    orders = filter_set.qs 
    return render(request, "webapp/order.html", {"filter": filter_set, "orders": orders})