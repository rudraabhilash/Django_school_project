from django.urls import path
from . import views

urlpatterns = [
    path('marksheet_form_submit', views.marksheetform, name='marksheet_form_submit'),
    path('marksheet/', views.marksheet, name='marksheet'),
    path('marksheetsuccess/',views.marksheetsuccess, name='marksheetsuccess'), 
    path('subject_view', views.subject_view, name='subject_view')
    
]
