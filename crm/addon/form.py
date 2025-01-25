from django import forms
from api.models import *



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
