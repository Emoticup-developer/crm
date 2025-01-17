from django.contrib import admin


from .models import *

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Machine)
admin.site.register(Company)
admin.site.register(Location)
admin.site.register(Ticket)
admin.site.register(TicketPriority)
admin.site.register(TicketSource)
admin.site.register(TicketType)
admin.site.register(Order)
admin.site.register(Localization)
