from django import forms
from api.models import *


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            "type",
            "source",
            "client",
            "handled_by",
            "email_sms_notification",
            "office",
            "machine",
            "subject",
            "additional_information",
            "photo",
            "video",
        ]
        widgets = {
            "type": forms.Select(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500"
                }
            ),
            "source": forms.Select(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500"
                }
            ),
            "client": forms.Select(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500"
                }
            ),
            "handled_by": forms.Select(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500"
                }
            ),
            "office": forms.Select(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500"
                }
            ),
            "machine": forms.Select(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500"
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500",
                    "placeholder": "Enter ticket subject",
                }
            ),
            "additional_information": forms.Textarea(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-green-500 focus:border-green-500",
                    "rows": 4,
                    "placeholder": "Provide any additional details",
                }
            ),
            "photo": forms.FileInput(
                attrs={
                    "class": "mt-1 block w-full text-sm text-gray-700 border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500"
                }
            ),
            "video": forms.FileInput(
                attrs={
                    "class": "mt-1 block w-full text-sm text-gray-700 border-gray-300 rounded-md shadow-sm focus:ring-green-500 focus:border-green-500"
                }
            ),
            "email_sms_notification": forms.CheckboxInput(
                attrs={
                    "class": "h-4 w-4 text-green-500 border-gray-300 rounded focus:ring-green-400"
                }
            ),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "source",
            "po_number",
            "additional_note",
            "client",
            "handled_by",
            "email_sms_notification",
            "office_delivery",
            "machine",
            "products",
            "documents",
        ]
        widgets = {
            "source": forms.Select(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                }
            ),
            "po_number": forms.TextInput(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500",
                    "placeholder": "Enter PO number",
                }
            ),
            "additional_note": forms.Textarea(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500",
                    "rows": 4,
                    "placeholder": "Enter additional notes",
                }
            ),
            "client": forms.Select(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                }
            ),
            "handled_by": forms.Select(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                }
            ),
            "email_sms_notification": forms.CheckboxInput(
                attrs={
                    "class": "h-4 w-4 text-blue-500 border-gray-300 rounded focus:ring-blue-400"
                }
            ),
            "office_delivery": forms.Select(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                }
            ),
            "machine": forms.Select(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                }
            ),
            "products": forms.Select(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500"
                }
            ),
            "documents": forms.Textarea(
                attrs={
                    "class": "mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500",
                    "rows": 4,
                    "placeholder": "Enter documents in JSON format",
                }
            ),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "account_id",
            "full_name",
            "gender",
            "date_of_birth",
            "photo",
            "email",
            "mobile_no",
            "username",
            "password",
            "status",
            "notify_via_email_sms",
        ]
        widgets = {
            "date_of_birth": forms.SelectDateWidget(years=range(1900, 2100)),
        }


class RattingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = "__all__"


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = "__all__"

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class OderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class LocalizationForm(forms.ModelForm):
    class Meta:
        model = Localization
        fields = "__all__"
