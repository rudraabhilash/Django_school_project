from django.shortcuts import render
from django.http import HttpResponse
from .forms import student_attendance_form
from .models import standard,schedule
from django.shortcuts import render, loader,redirect


# Create your views here.

# this function shows student attendance form to students
def student_attendance(request):
    return render(request,'student_attendance_form.html')

def student_attendance_entry_process(request):
    if request.method == 'POST':
        form = student_attendance_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('ATTENDANCE MARKED')


def Standard(request):
    cur = standard.objects.all().values()   
    template = loader.get_template('standard.html')
    context = {
        'data': cur,
    }
    return HttpResponse(template.render(context,request))      



def Schedule(request):
    cur = schedule.objects.all().values()   
    template = loader.get_template('schedule.html')
    context = {
        'data': cur,
    }
    return HttpResponse(template.render(context, request))

       
