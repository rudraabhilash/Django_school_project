from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import Event_Form
from django.views.decorators.csrf import csrf_exempt
from .models import Event_Table
#from django.shortcuts import get_object_or_404
#from django.template import RequestContext
# Create your views here.

@csrf_exempt
def event_form(request):
    template = loader.get_template('event_form.html')
    return HttpResponse(template.render())

#event form submit function

@csrf_exempt
def event_form_submit(request):
    if request.method == 'POST':
        form = Event_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("eventsubmit_form")
        else:
            #form = Event_Form()
            return HttpResponse("data not filled correctly!")
        
#event success page     
def submited_form(request):
     template = loader.get_template('eventsuccess.html')
     return HttpResponse(template.render())

#event detailing function
def event_details(request):
    mydetails= Event_Table.objects.values_list('id','event_name','event_date').distinct()
    template = loader.get_template('event_name_details.html')
    context = {
        'mydata':mydetails,
    }  
    return HttpResponse(template.render(context, request))  

def all_event_details(request, event_name):
    mydetails= Event_Table.objects.filter(event_name=event_name)
    
    template = loader.get_template('submit.html')
    context = {
        'mydata':mydetails,
    }  
    return HttpResponse(template.render(context, request)) 

def event_image(request, id):
    i = Event_Table.objects.filter(id=id)
    template = loader.get_template('images.html')
    context = {
        'i':i,
    }
    return HttpResponse(template.render(context, request))

def event_all_images(request):
    images=Event_Table.objects.filter()    #on using filter() all images will be shown
    template = loader.get_template('images.html')
    context = {
        'i':images,
    }
    return HttpResponse(template.render(context, request))
    

