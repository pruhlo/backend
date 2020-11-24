from .views import *
from django.urls import path

urlpatterns = [
    path('home_page', get_home_page)
]
