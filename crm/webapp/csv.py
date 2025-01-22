from django.http import HttpResponse
from openpyxl import Workbook
from api.models import *

from django.http import HttpResponse
from openpyxl import Workbook
from datetime import datetime
import json

def download_queryset_as_excel(request, queryset):
    if not queryset.exists():
        return HttpResponse("No data to export.", content_type="text/plain")

    model = queryset.model
    field_names = [field.name for field in model._meta.fields]

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Data Export"

    # Add headers
    sheet.append(field_names)

    # Add data rows
    for obj in queryset:
        row = []
        for field in field_names:
            value = getattr(obj, field, None)
            # If the field has no value, set it as "NA"
            if not value:
                value = "NA"
            # If it's a file or image field, check for the URL
            elif hasattr(value, 'url'):
                value = f"{request.scheme}://{request.get_host()}{value.url}" if value.name else "NA"
            # If it's a datetime field with timezone, remove the timezone info
            elif isinstance(value, datetime):
                if value.tzinfo is not None:
                    value = value.replace(tzinfo=None)  # Remove timezone info
                value = value.strftime("%Y-%m-%d %H:%M:%S")  # Format datetime as string
            # If it's a dictionary, convert it to a string (JSON string representation)
            elif isinstance(value, dict):
                value = json.dumps(value)  # Convert dictionary to JSON string
            # If it's a related model (foreign key), extract a field or string representation
            elif hasattr(value, '__str__'):
                value = str(value)  # Convert the related model to its string representation
            row.append(value)
        sheet.append(row)

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = f'attachment; filename="{model.__name__.lower()}_data.xlsx"'
    workbook.save(response)
    return response



def download_localization(request):
    return download_queryset_as_excel(request,Localization.objects.all())


def download_product(request):
    return download_queryset_as_excel(request,Product.objects.all())


def download_machine(request):
    return download_queryset_as_excel(request,Machine.objects.all())


def download_ticket(request):
    return download_queryset_as_excel(request,Ticket.objects.all())


def download_order(request):
    return download_queryset_as_excel(request,Order.objects.all())


def download_client(request):
    return download_queryset_as_excel(request,Client.objects.all())


def download_ratting(request):
    return download_queryset_as_excel(request,Rating.objects.all())


def download_company(request):
    return download_queryset_as_excel(request,Company.objects.all())



def download_location(request):
    return download_queryset_as_excel(request,Location.objects.all())
