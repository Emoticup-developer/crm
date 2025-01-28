from django import forms
from api.models import *


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


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
        

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"


class LocalizationForm(forms.ModelForm):
    class Meta:
        model = Localization
        fields = "__all__"




class TicketFileForm(forms.ModelForm):
    class Meta:
        model = TicketDocs
        fields = "__all__"

class OrderFileForm(forms.ModelForm):
    class Meta:
        model = OrderDocs
        fields = "__all__"
        

class MachineAttributesForm(forms.ModelForm):
    class Meta:
        model = machine_attributes
        fields = "__all__"







class CompanyMachineTableForm(forms.ModelForm):
    class Meta:
        model = CompanyMachineTable
        fields = ['machine', 'company', 'used_by']
        widgets = {
            'machine': forms.Select(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'used_by': forms.Select(attrs={'class': 'form-control'}),
        }




