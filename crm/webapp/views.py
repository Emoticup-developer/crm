from django.shortcuts import render
from api.models import *
from addon.filter import *
from .forms import *
from django.shortcuts import redirect
from .chart import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.conf import settings
from cryptography.fernet import Fernet
from django.contrib.auth import logout
from django.http import JsonResponse
from .models import LogsAndHistory

def user_logout(request):
    logout(request)

    return redirect("login")


@login_required(login_url="/login")
def index(request):
    context = chart_view()
    context["staff"] = Client.objects.filter(
        username__in=User.objects.filter(is_staff=True).values("username")
    ).count()
    context["clients"] = Client.objects.filter(
        username__in=User.objects.filter(is_staff=False).values("username")
    ).count()
    context["total_user"] = Client.objects.all().count()
    context["product"] = Product.objects.all().count()
    context["machine"] = Machine.objects.all().count()
    context["ticket"] = Ticket.objects.all().count()
    context["order"] = Order.objects.all().count()
    context["Reviews"] = Rating.objects.all().count()
    return render(request, "webapp/index.html", context)


def login_user(request):
    if request.method != "POST":
        return render(request, "webapp/login.html")

    username = request.POST.get("username")
    password = request.POST.get("password")

    if not username or not password:
        return JsonResponse({"error": "Username and password are required"}, status=400)

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("index")
    else:
        return JsonResponse({"error": "Invalid credentials"}, status=401)


@login_required
def logs(request):
    return render(
        request,
        "webapp/logs.html",
        context={"logs": LogsAndHistory.objects.order_by("-id").all()},
    )




@login_required
def localization(request):
    return render(
        request,
        "webapp/localization.html",
        context={
            "location": Location.objects.all(),
            "normal_user" : Client.objects.filter(username__in=User.objects.filter(is_staff=False).values_list('username', flat=True)).count(),  
            "staff":Client.objects.filter(username__in=User.objects.filter(is_staff=True).values_list('username', flat=True)).count(),
            "tickettype": TicketType.objects.all().count(),
            "ticketsource": TicketSource.objects.all().count(),
            "TicketPriority": TicketPriority.objects.all().count(),
            "TopBarIcon": TopBarIcon.objects.all().count(),
            "SideBarIcon": SideBarIcon.objects.all().count(),
            "OrderSource": OrderSource.objects.all().count(),
            "Rating": Rating.objects.all().count(),
            "Authorize": Authorize.objects.all().count(),
            "Country": Country.objects.all().count(),
            "State": State.objects.all().count(),
        },
    )


@login_required
def localization_create(request):
    if request.method == "POST":
        form = LocalizationForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = LocalizationForm()
    return render(request, "webapp/localization_form.html", {"form": form})


@login_required
def product(request):
    return render(
        request,
        "webapp/product.html",
        context={"product": Product.objects.filter(trash = False).all()},
    )


@login_required
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = ProductForm()
    return render(request, "webapp/createproduct.html", {"form": form})


@login_required
def machine(request):
    return render(
        request,
        "webapp/machine.html",
        context={"machine": Machine.objects.filter(trash = False).all()},
    )


@login_required
def machine_create(request):
    if request.method == "POST":
        form = MachineForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = MachineForm()
    return render(request, "webapp/createmachine.html", {"form": form,"location":Location.objects.all()})


@login_required
def ticket(request):
    filter_set = TicketFilter(request.GET, queryset=Ticket.objects.all())
    tickets = filter_set.qs 
    return render(
        request,
        "webapp/ticket.html",
        context={"ticket": Ticket.objects.filter(trash = False).all(),"filter":filter_set},
    )


@login_required
def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            messages.error(request, f"{form.errors}")
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
        "priority": TicketPriority.objects.all(),
    }
    return render(request, "webapp/createticket.html", context)


@login_required
def order(request):
    filter_set = OrderFilter(request.GET, queryset=Order.objects.all())
    orders = filter_set.qs 
    return render(
        request,
        "webapp/order.html",
        context={"orders": Order.objects.filter(trash = False).all(),"filter":filter_set},
    )


@login_required
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = OrderForm()

    sources = OrderSource.objects.all()
    clients = Client.objects.filter(trash = False).all()
    offices = Company.objects.filter(trash = False).all()
    machines = Machine.objects.filter(trash = False).all()
    products = Product.objects.filter(trash = False).all()
    handlers = Client.objects.filter(trash = False).all()

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


@login_required
def client(request):
    clients = Client.objects.filter(trash = False).all()
    return render(request, "webapp/client.html", {"clients": clients})


@login_required
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
            user.set_password(request.POST["password"])
            user.save()
            print("account created")
            return redirect("index")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = ClientForm()
    return render(request, "webapp/createclient.html", {"form": form})


@login_required
def ratting(request):
    clients = Rating.objects.filter(trash = False).all()
    return render(request, "webapp/ratting.html", {"ratting": clients})


@login_required
def view_ratting(request, id):
    return render(
        request,
        "webapp/view_rattings.html",
        context={
            "rating": Rating.objects.get(id=id),
        },
    )


@login_required
def view_ticket(request, id):
    return render(
        request,
        "webapp/view_ticket.html",
        context={
            "ticket": Ticket.objects.get(id=id),
            "docs": TicketDocs.objects.filter(
                associated=Ticket.objects.get(id=id)
            ).all(),
        },
    )


@login_required
def view_order(request, id):
    return render(
        request,
        "webapp/view_order.html",
        context={
            "order": Order.objects.get(id=id),
            "docs": OrderDocs.objects.filter(associated=Order.objects.get(id=id)).all(),
        },
    )


@login_required
def view_localization(request, id):
    return render(
        request,
        "webapp/view_localization.html",
        context={
            "localization": Localization.objects.get(id=id),
        },
    )


@login_required
def view_machine(request, id):
    return render(
        request,
        "webapp/view_machine.html",
        context={
            "machine": Machine.objects.get(id=id),
            "attributes": machine_attributes.objects.filter(
                associated=Machine.objects.get(id=id)
            ).all(),
        },
    )


@login_required
def view_product(request, id):
    return render(
        request,
        "webapp/view_product.html",
        context={
            "product": Product.objects.get(id=id),
        },
    )


@login_required
def view_client(request, id):
    return render(
        request,
        "webapp/view_client.html",
        context={
            "client": Client.objects.get(id=id),
        },
    )


@login_required
def view_location(request, id):
    return render(
        request,
        "webapp/view_location.html",
        context={
            "location": Location.objects.get(id=id),
        },
    )


@login_required
def view_company(request, id):
    return render(
        request,
        "webapp/view_company.html",
        context={
            "company": Company.objects.get(id=id),
        },
    )


@login_required
def company(request):
    clients = Company.objects.filter(trash = False).all()
    return render(request, "webapp/company.html", {"company": clients})


@login_required
def company_create(request):
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
        else:
            print(form.errors)
            return redirect("company_create")
    else:
        form = CompanyForm()
    return render(request, "webapp/company_create.html", {"form": form})


@login_required
def location(request):
    clients = Location.objects.filter(trash = False).all()
    return render(request, "webapp/location.html", {"location": clients})


@login_required
def location_create(request):
    if request.method == "POST":
        form = LocalizationForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("index")
    else:
        form = LocationForm()
    return render(request, "webapp/location_create.html", {"form": form})


@login_required
def profile(request):
    return render(
        request,
        "webapp/profile.html",
        context={
            "client": Client.objects.filter(username=request.user.username,trash = False).first(),
        },
    )


@login_required
def password_reset(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if new_password == confirm_password:
                user.set_password(confirm_password)
                messages.success(request, "password reset successfully ")
                return redirect("profile")
            else:
                messages.error(request, "password not matching......")
    return render(request, "webapp/reset.html")


@login_required
def order_docs_create(request):
    if request.method == "POST":
        form = OrderFileForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("view_order", id=request.POST.get("associated"))
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = OrderFileForm()
    return render(request, "webapp/createmachine.html", {"form": form})


@login_required
def ticket_docs_create(request):
    if request.method == "POST":
        form = TicketFileForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("view_ticket", id=request.POST.get("associated"))
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = TicketFileForm()
    return render(request, "webapp/createmachine.html", {"form": form})


@login_required
def add_machine_attribute(request):
    if request.method == "POST":
        form = MachineAttributesForm(request.POST, request.FILES)
        if form.is_valid():
            client = form.save()
            client.save()
            return redirect("view_machine", id=request.POST.get("associated"))
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = MachineAttributesForm()
    return render(request, "webapp/createmachine.html", {"form": form})


def authorize(request):
    if request.method == "POST":
        shakey = Fernet.generate_key().decode("utf-8")
        responce = render(
            request,
            "webapp/authorize.html",
            context={
                "key": shakey,
            },
        )
        responce.set_cookie(
            "secure_key",
            shakey,
            httponly=True,
            secure=False,  # Set to False for local testing
            samesite="Strict",
            max_age=60 * 60 * 24 * 60,
        )
        return responce
    return render(request, "webapp/authorize.html")




@login_required
def company_assign(request):
    if request.method == 'POST':
        form = CompanyMachineTableForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record added successfully!")
            return redirect('company_assign_view')
    else:
        form = CompanyMachineTableForm()
    return render(request, 'webapp/company_asign.html', {'form': form})



@login_required
def company_assign_view(request):
    return render(
        request,
        "webapp/company_assign_view.html",
        context={"company_machine_records": CompanyMachineTable.objects.all()},
    )
