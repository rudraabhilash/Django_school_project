from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('attendence.urls')),
    path('',include('marksheet.urls')),
    path('',include('user.urls')),
    path('',include('Fee.urls')),
    path('',include('event.urls')),
    path('',include('games.urls')),
    path('',include('student_parent.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

