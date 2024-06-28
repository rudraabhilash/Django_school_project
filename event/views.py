from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import Event_Form
from django.views.decorators.csrf import csrf_exempt
from .models import Event_Table, Event_Image
# Create your views here.

@csrf_exempt
def event_registration(request):
    template = loader.get_template('event_form.html')
    return HttpResponse(template.render())

#event form submit function

@csrf_exempt
def event_form_submit(request):
    if request.method == 'POST':
        form = Event_Form(request.POST, request.FILES)
        
        if form.is_valid():
            events=form.save(commit=False)
            images = request.FILES.getlist('event_image_location')
            events.save()
            
            for image in images:
                event_image = Event_Image.objects.create(event_table=events, event_image_location=image)
            return redirect("eventsubmit_form")
        else:
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

def specific_event_details(request, event_name):
    mydetails= Event_Table.objects.filter(event_name=event_name)
    template = loader.get_template('specific_event.html')
    context = {
        'mydata':mydetails,
    }  
    return HttpResponse(template.render(context, request)) 

def event_image(request, id):
    single_event_image = Event_Image.objects.filter(event_table_id=id)
    single_event_table = Event_Table.objects.filter(id=id)
    template = loader.get_template('images.html')
    context = {
        'images':single_event_image,
        'ids':single_event_table,
    }
    return HttpResponse(template.render(context, request))

def event_all_images(request):
    all_images=Event_Image.objects.all()    #on using filter() all images will be shown
    all_ids = Event_Table.objects.filter()
    template = loader.get_template('images.html')
    context = {
        'images':all_images,
        'ids':all_ids,
    }
    return HttpResponse(template.render(context, request))
    
