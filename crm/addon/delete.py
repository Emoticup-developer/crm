from api.models import *
from django.shortcuts import redirect
from django.contrib import messages

def delete_company(request,id):
    obj = Company.objects.get(id=id)
    obj.trash = True
    obj.save()
    return redirect("company")



def delete_ticket(request,id):
    obj = Ticket.objects.get(id=id)
    obj.trash = True
    obj.save()
    return redirect("ticket")



def delete_order(request,id):
    obj = Order.objects.get(id=id)
    obj.trash = True
    obj.save()
    return redirect("order")



def delete_product(request,id):
    obj = Product.objects.get(id=id)
    obj.trash = True
    obj.save()
    return redirect("product")


def delete_machine(request,id):
    obj = Machine.objects.get(id=id)
    obj.trash = True
    obj.save()
    return redirect("machine")



def delete_location(request,id):
    obj = Location.objects.get(id=id)
    obj.trash = True
    obj.save()
    return redirect("location")


def delete_client(request,id):
    obj = Client.objects.get(id=id)
    obj.trash = True
    obj.save()
    return redirect("location")