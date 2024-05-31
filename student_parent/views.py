from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .forms import formDataToTableColMap, formParaentDataToTableCoMap
from .models import Student, Parent
	
def student(request):
    return render(request,'studentRegistration.html')
@csrf_exempt
def submitform1(response):
    #return HttpResponse(response.POST)
    template = loader.get_template('parent_form.html')
    if response.method == 'POST':
        form = formDataToTableColMap(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(template.render())
        else:
            return HttpResponse("data not filled correctlly!")
@csrf_exempt       
def submitform2(response):  
    if response.method == 'POST':
        forms = formParaentDataToTableCoMap(response.POST)
        if forms.is_valid():
            forms.save()
            return render(response,'student_success.html')
        else:
            return HttpResponse("data not filled correctlly!")      

def studentDetail(request):
    sdetails = Student.objects.all().values()
    template = loader.get_template('student.html')
    context = {
        'sdetails':sdetails
    }
    return HttpResponse(template.render(context,request))

def parentDetail(request):
    pdetails = Parent.objects.all().values()
    template = loader.get_template('parent.html')
    context = {
        'pdetails':pdetails
    }
    return HttpResponse(template.render(context,request))