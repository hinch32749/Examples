from django.urls import path

from .views import fn


urlpatterns = [
    path('', fn, name="fn")
]