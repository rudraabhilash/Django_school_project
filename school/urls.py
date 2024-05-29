from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('attendence.urls')),
    path('',include('marksheet.urls')),
    path('',include('user.urls')),
    path('',include('Fee.urls')),
    path('',include('event.urls')),
    path('',include('games.urls')),
    path('',include('student_parent.urls')),
]
