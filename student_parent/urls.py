from django.urls import path
from . import views

urlpatterns = [
    path('student_parent/', views.student, name='Student'),
    path('submitform_student/', views.submitform1, name='submitform1'),
    path('submitform_parent/', views.submitform2, name='submitform2'),
    path('student_details/', views.studentDetail, name='studentDetail'),
    path('parent_details/', views.parentDetail, name='parentDetail'),
]