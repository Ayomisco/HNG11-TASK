from django.urls import path
from .views import get_basic_info

urlpatterns = [
    path('info/', get_basic_info, name='hello'),
]
