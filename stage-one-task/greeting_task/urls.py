# greeting_task/urls.py
from django.contrib import admin
from django.urls import path, include  # include is used to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hello.urls')),  # Include URLs from the hello app
]
