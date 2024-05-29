from django.urls import path
from . import views

urlpatterns = [
    path('event/', views.event_form, name='event'),
    path('event_submit/', views.event_form_submit, name='event_submit'),
    path('eventsubmit_form/', views.submited_form, name='eventsubmit_form'),
    path('event_details/', views.event_details, name='event_details'),
]


