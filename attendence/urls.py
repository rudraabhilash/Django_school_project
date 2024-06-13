from django.urls import path
from . import views

urlpatterns = [


path('student_attendance/',views.student_attendance,name='student_attendance'),
path('student_attendance_entry_process/',views.student_attendance_entry_process,name='student_attendance_entry_process'),
path('student_attendance_response/',views.student_attendance_response,name='student_attendance_response'),

path('standard/',views.Standard,name='Standard'),
path('schedule/',views.Schedule,name='Schedule'),
path('attendance_record/',views.attendance_record,name='attendance_record'),
path('attendance_record_process/',views.attendance_record_process,name='attendance_record_process'),
]