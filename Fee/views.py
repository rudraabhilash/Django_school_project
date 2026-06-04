from .models import Payment, Fee_details
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import PaymentForm
from django.views.decorators.csrf import csrf_exempt 
import razorpay
from school.settings import key, secret

#fees function
@csrf_exempt
def fees(request):
  template = loader.get_template('payment_details.html')
  return HttpResponse(template.render())

#payment_form function
@csrf_exempt
def payment_form(request):
    if request.method == 'POST':
        razorpay_client = razorpay.Client(auth=(key, secret))
        
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            payment = razorpay_client.order.create({
              'amount':int(request.POST.get('fee_paid'))*100,
              'currency':'INR',
              'payment_capture':'1'
            })
            print('*********************')
            print(payment)
            print('*********************')
            template = loader.get_template('payment_page.html')
            context = {
                'payment': payment,
            }
            return HttpResponse(template.render(context, request))
            # return redirect("feesuccess")
        else:
            return HttpResponse(form)
            

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
  myfee = Payment.objects.all().values('student_id','fee_paid')
  template = loader.get_template('fee_details.html')
  context = {
    'myfee': myfee,
  }
  return HttpResponse(template.render(context, request))


