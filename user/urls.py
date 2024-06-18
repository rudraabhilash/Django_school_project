from django.urls import path
from . import views

urlpatterns = [
    path('createaccount/', views.members, name='createaccount'),
    path('usersubmit', views.details, name='usersubmit'),
    path('login/', views.members1, name='login'),
    path('yourdetails', views.members2, name='yourdetails'),
    path('logout',views.logout,name='logout'),
    
]