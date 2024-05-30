from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Marksheet, Subject

@csrf_exempt
def welcome(request):
    return render(request, 'welcome.html')

def marksheet(request):
    return render(request, 'marksheet.html')

@csrf_exempt
def submitform_process(request):
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

def marksheetsuccess(request):
    markstorage = Marksheet.objects.all().values()
    template = loader.get_template('marksheetsuccess.html')
    context = {
        'markstorage': markstorage,
    }
    return HttpResponse(template.render(context, request))

def subject_view(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_template.html', {'subjects': subjects})
