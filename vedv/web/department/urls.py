from .views import *
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about_vedv', get_home_page, name="about_vedv"),
    path('', get_start_page, name="start_page"),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)