from django.shortcuts import render
from api.models import *
from .forms import *
from django.shortcuts import redirect
from .chart import *
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    context = chart_view()
    return render(request, "webapp/index.html", context)


def login(request):
    return render(request, "webapp/login.html")


def localization(request):
    return render(
        request,
        "webapp/localization.html",
        context={"localizations": Localization.objects.all()},
    )


def localization_create(request):
    if request.method == "POST":
        form = LocalizationForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
    else:
        form = LocalizationForm()
    return render(request, "webapp/localization_form.html", {"form": form})


def product(request):
    return render(
        request,
        "webapp/product.html",
        context={"product": Product.objects.all()},
    )


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
    else:
        form = ProductForm()
    return render(request, "webapp/createproduct.html", {"form": form})


def machine(request):
    return render(
        request,
        "webapp/machine.html",
        context={"machine": Machine.objects.all()},
    )


def machine_create(request):
    if request.method == "POST":
        form = MachineForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
    else:
        form = MachineForm()
    return render(request, "webapp/createmachine.html", {"form": form})


def ticket(request):
    return render(
        request,
        "webapp/ticket.html",
        context={"ticket": Ticket.objects.all()},
    )


def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = TicketForm()

    context = {
        "form": form,
        "ticket_types": TicketType.objects.all(),
        "ticket_sources": TicketSource.objects.all(),
        "clients": Client.objects.all(),
        "handlers": Client.objects.all(),
        "offices": Company.objects.all(),
        "machines": Machine.objects.all(),
    }
    return render(request, "webapp/createticket.html", context)


def order(request):
    return render(
        request,
        "webapp/order.html",
        context={"orders": Order.objects.all()},
    )


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = OrderForm()

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
    return render(request, "webapp/createorder.html", context)


def client(request):
    clients = Client.objects.all()
    return render(request, "webapp/client.html", {"clients": clients})


def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():

            client = form.save()
            client.save()
            print("data saved")
            user = User.objects.create(
                username=request.POST["username"],
                password=request.POST["password"],
                email=request.POST["email"],
            )
            user.save()
            print("account created")
            return redirect("index")
    else:
        form = ClientForm()
    return render(request, "webapp/createclient.html", {"form": form})


def ratting(request):
    clients = Rating.objects.all()
    return render(request, "webapp/ratting.html", {"ratting": clients})


def view_ratting(request, id):
    return render(
        request,
        "webapp/view_rattings.html",
        context={
            "rating": Rating.objects.get(id=id),
        },
    )


def view_ticket(request, id):
    return render(
        request,
        "webapp/view_ticket.html",
        context={
            "ticket": Ticket.objects.get(id=id),
        },
    )


def view_order(request, id):
    return render(
        request,
        "webapp/view_order.html",
        context={
            "order": Order.objects.get(id=id),
        },
    )


def view_localization(request, id):
    return render(
        request,
        "webapp/view_localization.html",
        context={
            "localization": Localization.objects.get(id=id),
        },
    )


def view_machine(request, id):
    return render(
        request,
        "webapp/view_machine.html",
        context={
            "machine": Machine.objects.get(id=id),
        },
    )


def view_product(request, id):
    return render(
        request,
        "webapp/view_product.html",
        context={
            "product": Product.objects.get(id=id),
        },
    )


def view_client(request, id):
    return render(
        request,
        "webapp/view_client.html",
        context={
            "client": Client.objects.get(id=id),
        },
    )
