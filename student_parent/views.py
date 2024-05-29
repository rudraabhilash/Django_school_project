from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import formDataToTableColMap, formParaentDataToTableCoMap
from .models import Student, Parent
	
def student(request):
    return render(request,'studentRegistration.html')

def submitform1(response):
    #return HttpResponse(response.POST)
    if response.method == 'POST':
        form = formDataToTableColMap(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Data successfully inserted!")
        else:
            return HttpResponse("data not filled correctlly!")
        
def submitform2(request):  
    if request.method == 'POST':
        forms = formParaentDataToTableCoMap(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponse("Data successfully inserted!")
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