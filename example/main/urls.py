import os

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import login, navigate, open_button, links_login


urlpatterns = [
    path('log/', login, name='login'),
    path('nav/', navigate, name='navigate'),
    path('open_button/', open_button, name='open_button'),
    path('links_login', links_login, name='links_login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
