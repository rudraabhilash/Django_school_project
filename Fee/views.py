from .models import Payment, Fee_details
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import PaymentForm
from django.views.decorators.csrf import csrf_exempt 

import io
from django.template.loader import get_template
from xhtml2pdf import pisa
from datetime import datetime

#fees function
@csrf_exempt
def fees(request):
  template = loader.get_template('payment_details.html')
  return HttpResponse(template.render())

#payment_form function
@csrf_exempt
def payment_form(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("feesuccess")
        else:
            return HttpResponse(form)
            return render(request, 'myfirst.html', {'form': form})

#feesuccess function
def feesuccess(request):
   paymentstatus = Payment.objects.all().values()
   template = loader.get_template('feesuccess.html')
   context = {
       'paymentstatus': paymentstatus
   }
   return HttpResponse(template.render(context, request))

#fee_details function
def fee_details(request):
  myfee = Fee_details.objects.all().values()
  template = loader.get_template('fee_details.html')
  context = {
    'myfee': myfee,
  }
  return HttpResponse(template.render(context, request))

def fetch_data(request):
    if request.method == 'POST':
        student_id= request.POST.get('student_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        return redirect('show_data', student_id=student_id, start_date=start_date, end_date=end_date) #change this name of url
    return render(request, 'fetch_data.html')
def show_data(request, student_id, start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    data = Payment.objects.filter(student_id=student_id, date_of_payment__range=[start_date, end_date])
    return render(request, 'show_data.html', {'data': data, 'student_id': student_id, 'start_date': start_date, 'end_date': end_date})

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def download_pdf(request, student_id, start_date, end_date):
    data = Payment.objects.filter(student_id=student_id, date_of_payment__range=[start_date, end_date])
    context = {
        'data': data,
        'student_id': student_id,
        'start_date': start_date,
        'end_date': end_date
    }
    pdf = render_to_pdf('pdf_template.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="data_{student_id}.pdf"'
        return response
    return HttpResponse("Error generating PDF")
