from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
urlpatterns = [
    path('', get_home),
    path('protocols', get_protocols, name='protocols'),
    # path('analis', get_analis),
    # path('analis/get_analis<df_list>', get_analis),
    # path('describe/get_analis<df_list>/', get_analis, name='get_analis'),
    path('describe', get_analis, name='get_analis'),
    # url(r'^describe/describe-(?P<parameter>[\w-]+).html', 'views.product', name="product"),
    
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

