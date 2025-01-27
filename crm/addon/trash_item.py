from django.shortcuts import render
from api.models import *
from django.contrib.auth.decorators import login_required
from .form import *
from django.shortcuts import redirect
from django.contrib import messages


@login_required
def product_trash(request):
    return render(
        request,
        "webapp/product.html",
        context={"product": Product.objects.filter(trash = True).all()},
    )
    
    
@login_required
def machine_trash(request):
    return render(
        request,
        "webapp/machine.html",
        context={"machine": Machine.objects.filter(trash = True).all()},
    )


@login_required
def ticket_trash(request):
    filter_set = TicketFilter(request.GET, queryset=Ticket.objects.all())
    tickets = filter_set.qs 
    return render(
        request,
        "webapp/ticket.html",
        context={"ticket": Ticket.objects.filter(trash = True).all(),"filter":filter_set},
    )



@login_required
def order_trash(request):
    filter_set = OrderFilter(request.GET, queryset=Order.objects.all())
    orders = filter_set.qs 
    return render(
        request,
        "webapp/order.html",
        context={"orders": Order.objects.filter(trash = True).all(),"filter":filter_set},
    )


@login_required
def client_trash(request):
    clients = Client.objects.filter(trash = True).all()
    return render(request, "webapp/client.html", {"clients": clients})




@login_required
def ratting_trash(request):
    clients = Rating.objects.filter(trash = True).all()
    return render(request, "webapp/ratting.html", {"ratting": clients})



@login_required
def company_trash(request):
    clients = Company.objects.filter(trash = True).all()
    return render(request, "webapp/company.html", {"company": clients})



@login_required
def location_trash(request):
    clients = Location.objects.filter(trash = True).all()
    return render(request, "webapp/location.html", {"location": clients})