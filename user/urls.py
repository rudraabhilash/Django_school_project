from django.urls import path
from . import views

urlpatterns = [
    path('signup_page/', views.show_signup_form, name='signup'),
    path('create_account/', views.signup_view, name='create_account'),
    path('login/', views.login_view, name='login'),
    path('yourdetails', views.user_details_view, name='yourdetails'),
    path('auth/', views.auth_view, name='auth'),
    path('logout/', views.logout_view, name='logout')
    
]