from django.urls import path
from . import views

urlpatterns = [
     path('fees/', views.fees, name='fees'),
     path('feesubmitform', views.payment_form, name='feesubmitform'),
     path('feesuccess', views.feesuccess, name='feesuccess'),
     path('fee_details/', views.fee_details, name='fee_details'),

]