from django.shortcuts import render
from api.models import *
from django.contrib.auth.decorators import login_required
from .form import *
from django.shortcuts import redirect
from django.contrib import messages


# ---------------------------------------------------------------------------------

@login_required
def add_ticket(request):
    return render(request,"addon/add_ticket.html",context={
        "tickets":TicketType.objects.all()
    })

@login_required
def add_ticket_form(request):
    if request.method == "POST":
        form = TicketTypeAddForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("add_ticket")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = TicketTypeAddForm()
    return render(request,"addon/add_ticket_form.html",context={
        "form":form,
    })

# ---------------------------------------------------------------------
@login_required
def ticket_source(request):
    return render(request,"addon/ticket_source.html",context={
        "ticket_sources":TicketSource.objects.all()
    })

@login_required
def ticket_source_form(request):
    if request.method == "POST":
        form = TicketSourceAddForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("ticket_source")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = TicketSourceAddForm()
    return render(request,"addon/ticket_source_form.html",context={
        "form":form,
    })


# ----------------------------------------------------------------------------------


@login_required
def ticket_priorities(request):
    return render(request,"addon/ticket_priorities.html",context={
        "ticket_priorities":TicketPriority.objects.all()
    })



@login_required
def ticket_priorities_form(request):
    if request.method == "POST":
        form = TicketPriorityAddForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("ticket_priorities")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = TicketPriorityAddForm()
    return render(request,"addon/ticket_priorities_form.html",context={
        "form":form,
    })

# -------------------------------------------------------------------------------

@login_required
def country(request):
    return render(request,"addon/country.html",context={
        "countries":Country.objects.all()
    })

@login_required
def country_form(request):
    if request.method == "POST":
        form = CountryAddForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("country")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = CountryAddForm()
    return render(request,"addon/country_form.html",context={
        "form":form,
    })



# ---------------------------------------------------------------------------------

@login_required
def states(request):
    return render(request,"addon/states.html",context={
        "states":State.objects.all()
    })

@login_required
def states_form(request):
    if request.method == "POST":
        form = StateAddForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("states")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = StateAddForm()
    return render(request,"addon/states_form.html",context={
        "form":form,
        "countries":Country.objects.all()
    })


# ----------------------------------------------------------------------------------------

@login_required
def order_source(request):
    return render(request,"addon/order_source.html",context={
        "order_sources":OrderSource.objects.all()
    })


@login_required
def order_source_form(request):
    if request.method == "POST":
        form = OrderSOurceAddForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("order_source")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = OrderSOurceAddForm()
    return render(request,"addon/order_source_form.html",context={
        "form":form,
    })
    
    


@login_required
def ticket_stats(request):
    return render(request,"addon/ticket_stats.html",context={
        "order_sources":TicketStatus.objects.all()
    })


@login_required
def ticket_stats_form(request):
    if request.method == "POST":
        form = TicketStatusForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("ticket_stats")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = TicketStatusForm()
    return render(request,"addon/ticket_stats_form.html",context={
        "form":form,
    })
    
    
    



@login_required
def order_status(request):
    return render(request,"addon/order_status.html",context={
        "order_status":OrderStatus.objects.all()
    })


@login_required
def order_status_from(request):
    if request.method == "POST":
        form = OrderStatusForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("order_status")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = OrderStatusForm()
    return render(request,"addon/order_status_from.html",context={
        "form":form,
    })