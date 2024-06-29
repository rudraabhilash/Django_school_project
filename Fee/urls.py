from django.urls import path
from . import views

urlpatterns = [
     path('fees/', views.fees, name='fees'),
     path('feesubmitform', views.payment_form, name='feesubmitform'),
     path('feesuccess', views.feesuccess, name='feesuccess'),
     path('fee_details/', views.fee_details, name='fee_details'),
     path('fetch_data/', views.fetch_data, name='fetch_data'),
     path('show_data/<str:student_id>/<str:start_date>/<str:end_date>/', views.show_data, name='show_data'),
     path('download_pdf/<str:student_id>/<str:start_date>/<str:end_date>/', views.download_pdf, name='download_pdf'),
]