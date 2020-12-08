from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', get_home),
    path('protocols', get_protocols, name='protocols'),
    path('describe', get_analis, name='get_analis'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

