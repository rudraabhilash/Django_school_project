from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Marksheet, Subject 

@csrf_exempt
def welcome(request):
    return render(request, 'welcome.html')

def marksheet(request):
    if request.session.has_key('user'):
        c=1
    else:
        c=0
    context={
        'c':c,
        
    }    
    template = loader.get_template('marksheet.html')
    return HttpResponse(template.render(context, request))

    

@csrf_exempt
def submitform_process(request):
  if request.session.has_key('user'):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        english_marks = request.POST.get('english_marks')
        hindi_marks = request.POST.get('hindi_marks')
        maths_marks = request.POST.get('maths_marks')
        science_marks = request.POST.get('science_marks')
        socialstudy_marks = request.POST.get('socialstudy_marks')
        session = request.POST.get('session')

        temp = Marksheet(
            student_id=student_id,
            english_marks=english_marks,
            hindi_marks=hindi_marks,
            maths_marks=maths_marks,
            science_marks=science_marks,
            socialstudy_marks=socialstudy_marks,
            session=session
        )
        temp.save()
        return redirect("/marksheetsuccess")  # Assuming this is the URL for success page
    else:
        return HttpResponse("Invalid request method.")
  else:  
   return render(request, 'marksheet.html', {'error_message': 'please login'}) 
 
    

def marksheetsuccess(request):
 if request.session.has_key('user'):
    markstorage = Marksheet.objects.all().values()

    template = loader.get_template('marksheetsuccess.html')
    context = {
        'markstorage': markstorage,
    }
    return HttpResponse(template.render(context, request))
 else:
     return render(request, 'some.html', {'error_message': 'please login'})
        

def subject_view(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_template.html', {'subjects': subjects})



#-----------------------------------------------------------------------------------#
from django.shortcuts import render
from .forms import MarksheetForm
from .models import Marksheet
@csrf_exempt
def marksheet_view(request):
    if request.session.has_key('user'): 
        marksheet = None
        if request.method == 'POST':
            form = MarksheetForm(request.POST)
            if form.is_valid():
                student_id = form.cleaned_data['student_id']
                session = form.cleaned_data['session']
            
                
                # ORM query to fetch the marksheet
                marksheet = Marksheet.objects.filter(student_id=student_id, session=session)
        else:
            form = MarksheetForm()

        return render(request, 'marksheet_form.html', {'form': form, 'marksheet': marksheet})
    else:
        return redirect('/login')
