from django.shortcuts import render
from api.models import *
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def localization_update(request,id):
    if request.method == "POST":
        form = LocalizationForm(
            request.POST,
            request.FILES,
            instance=Localization.objects.filter(name=request.POST["name"]).first(),
        )
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
    else:
        form = LocalizationForm(instance=Localization.objects.filter(id=id).first())
    return render(request, "webapp/localization_update.html", {"form": form})

@login_required
def product_update(request,id):
    if request.method == "POST":
        form = ProductForm(
            request.POST,
            request.FILES,
            instance=Product.objects.filter(product_code=request.POST["product_code"]).first(),
        )
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
    else:
        form = ProductForm(instance=Product.objects.filter(id=id).first())
    return render(request, "webapp/product_update.html", {"form": form})

@login_required
def machine_update(request,id):
    if request.method == "POST":
        form = MachineForm(
            request.POST,
            request.FILES,
            instance=Machine.objects.filter(machine_id=request.POST["machine_id"]).first(),
        )
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
    else:
        form = MachineForm(instance=Machine.objects.filter(id=id).first())
    return render(request, "webapp/machine_update.html", {"form": form})


from django.shortcuts import get_object_or_404
@login_required
def ticket_update(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)

        if form.is_valid():
            form.save()
            print("data saved")
            return redirect("index")
    else:
        form = TicketForm(instance=ticket)

    context = {
        "form": form,
        "ticket_types": TicketType.objects.all(),
        "ticket_sources": TicketSource.objects.all(),
        "clients": Client.objects.all(),
        "handlers": Client.objects.all(),
        "offices": Company.objects.all(),
        "machines": Machine.objects.all(),
    }

    return render(request, "webapp/ticket_update.html", context)




@login_required
def order_update(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES, instance=order)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = OrderForm(instance=order)

    sources = OrderSource.objects.all()
    clients = Client.objects.all()
    offices = Company.objects.all()
    machines = Machine.objects.all()
    products = Product.objects.all()
    handlers = Client.objects.all()

    context = {
        "form": form,
        "sources": sources,
        "clients": clients,
        "offices": offices,
        "machines": machines,
        "products": products,
        "handlers": handlers,
    }

    return render(request, "webapp/order_update.html", context)



@login_required
def client_update(request,id):
    if request.method == "POST":
        form = ClientForm(
            request.POST,
            request.FILES,
            instance=Client.objects.filter(account_id=request.POST["account_id"]).first(),
        )
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
    else:
        form = ClientForm(instance=Client.objects.filter(id=id).first())
    return render(request, "webapp/client_update.html", {"form": form})







@login_required
def client_company(request,id=None):
    if request.method == "POST":
        form = CompanyForm(
            request.POST,
            request.FILES,
            instance=Company.objects.filter(company_name=request.POST["company_name"]).first(),
        )
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
        else:
            print(form.errors)
    else:
        form = CompanyForm(instance=Company.objects.filter(id=id).first())
    return render(request, "webapp/client_company.html", {"form": form})





@login_required
def client_location(request,id):
    if request.method == "POST":
        form = LocationForm(
            request.POST,
            request.FILES,
            instance=Location.objects.filter(title=request.POST["title"]).first(),
        )
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
    else:
        form = LocationForm(instance=Location.objects.filter(id=id).first())
    return render(request, "webapp/client_location.html", {"form": form,"company":Company.objects.all()})
