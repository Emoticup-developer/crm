from django import forms
from api.models import *
from .filter import *


class TicketTypeAddForm(forms.ModelForm):
    class Meta:
        model = TicketType
        fields = "__all__"


class TicketSourceAddForm(forms.ModelForm):
    class Meta:
        model = TicketSource
        fields = "__all__"



class TicketPriorityAddForm(forms.ModelForm):
    class Meta:
        model = TicketPriority
        fields = "__all__"



class CountryAddForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"




class StateAddForm(forms.ModelForm):
    class Meta:
        model = State
        fields = "__all__"


class OrderSOurceAddForm(forms.ModelForm):
    class Meta:
        model = OrderSource
        fields = "__all__"





class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = OrderStatus
        fields = "__all__"


class TicketStatusForm(forms.ModelForm):
    class Meta:
        model = TicketStatus
        fields = "__all__"




class TicketFilterForm(forms.Form):
    ticket_id = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ticket ID"}),
    )
    type = forms.ModelChoiceField(
        queryset=TicketType.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    source = forms.ModelChoiceField(
        queryset=TicketSource.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    priority = forms.ModelChoiceField(
        queryset=TicketPriority.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    status = forms.ModelChoiceField(
        queryset=TicketStatus.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    created_at_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="Created From",
    )
    created_at_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="Created To",
    )

class OrderFilterForm(forms.Form):
    order_id = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Order ID"}),
    )
    po_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "PO Number"}),
    )
    dc_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "DC Number"}),
    )
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    source = forms.ModelChoiceField(
        queryset=OrderSource.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    machine = forms.ModelChoiceField(
        queryset=Machine.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    status = forms.ModelChoiceField(
        queryset=OrderStatus.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    order_date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="Order Date From",
    )
    order_date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="Order Date To",
    )
