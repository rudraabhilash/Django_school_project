from django.shortcuts import redirect, render
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from .forms import student_attendance_form
from .models import standard, schedule, attendance
from datetime import datetime, timedelta

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_attendance(request):
    if request.session.has_key('user'):
        c=1
    else:
        c=0
    context={
        'c':c,
        
    }    
    template = loader.get_template('student_attendance_form.html')
    return HttpResponse(template.render(context, request))

    

@csrf_exempt
def student_attendance_entry_process(request):
    if request.session.has_key('user'):
     if request.method == 'POST':
        form = student_attendance_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student_attendance_response')
     else:
        form = student_attendance_form()
        return render(request, 'student_attendance_form.html', {'form': form})
    else:
        return render(request, 'student_attendance_form.html', {'error_message': 'please login.'})

@csrf_exempt
def Standard(request):
    if request.session.has_key('user'):
     cur = standard.objects.all().values()
     template = loader.get_template('standard.html')
     context = {
        'data': cur,
     }
     return HttpResponse(template.render(context, request))
    else:
         return render(request, 'student_attendance_form.html', {'error_message': 'please login.'})

@csrf_exempt
def Schedule(request):
    cur = schedule.objects.all().values()
    template = loader.get_template('schedule.html')
    context = {
        'data': cur,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def student_attendance_response(request):
    fetched = attendance.objects.all().values()
    template = loader.get_template('student_attendence_response.html')
    context = {
        'temp': fetched,
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def attendance_record(request):
    if request.session.has_key('user'):
     return render(request, 'attendance_record_page.html')
    else:
         return render(request, 'student_attendance_form.html', {'error_message': 'please login.'})
@csrf_exempt
def attendance_record_process(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return HttpResponse("Invalid date format. Please use YYYY-MM-DD.")

        # Generate all dates in the range
        total_days = (end_date - start_date).days + 1
        all_dates = [start_date + timedelta(days=i) for i in range(total_days)]

        # Fetch attendance records for the given date range
        attendance_records = attendance.objects.filter(
            student_id=student_id,
            date__range=[start_date, end_date]
        ).values('date')
        
        # Get the dates that have attendance records
        present_dates = {record['date'] for record in attendance_records}
        
        # Determine missing dates
        missing_dates = [date for date in all_dates if date not in present_dates]

        # Combine missing and present dates
        combined_dates = sorted(list(present_dates | set(missing_dates)))

        template = loader.get_template('record_stud_list.html')
        context = {
            'combined_dates': combined_dates,
            'student_id': student_id,
            'start_date': start_date,
            'end_date': end_date,
            'present_dates': present_dates
        }

        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("Invalid request method.")
