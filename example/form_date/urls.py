from django.urls import path

from .views import get_date


urlpatterns = [
    path('', get_date, name='get_date'),
]
