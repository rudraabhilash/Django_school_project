from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('submitform_process', views.submitform_process, name='submitform_process'),
    path('marksheet/', views.marksheet, name='marksheet'),
    path('marksheetsuccess/',views.marksheetsuccess, name='marksheetsuccess'),
    path('subject_view', views.subject_view, name='subject_view')
    
]