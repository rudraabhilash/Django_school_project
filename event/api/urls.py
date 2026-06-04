from django.urls import path
from . import views

urlpatterns = [
    path('api/events_list', views.events_list, name='events_list'),
]