from .views import *
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home_page', get_home_page, name="home_page"),
    path('', get_start_page, name="start_page"),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)