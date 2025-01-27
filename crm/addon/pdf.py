from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from api.models import *

def render_to_pdf(template_src,name, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{name}.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def generate_pdf_product(request,id):
    context = {
        "product":Product.objects.get(id=id)
    }
    return render_to_pdf('addon/pdf_product.html',"product", context)



def generate_pdf_machine(request,id):
    context = {
        "machine":Machine.objects.get(id=id)
    }
    return render_to_pdf('addon/generate_pdf_machine.html',"machine", context)



def generate_pdf_ticket(request,id):
    context = {
        "ticket":Ticket.objects.get(id=id)
    }
    return render_to_pdf('addon/generate_pdf_ticket.html',"ticket", context)



def generate_pdf_order(request,id):
    context = {
        "order":Order.objects.get(id=id)
    }
    return render_to_pdf('addon/generate_pdf_order.html',"orders", context)




