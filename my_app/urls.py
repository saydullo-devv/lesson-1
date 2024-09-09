
from django.urls import path
from .views import first_page, Madaminbek_page, ikkinchi_page, qaygusi_page, uchinchi_page, buyuk_page

urlpatterns = [
    path('', first_page, name='first_page'),
    path('kitob/1', Madaminbek_page, name='madaminbek_page'),
    path('kitob/2', qaygusi_page, name='qaygusi_page'),
    path('ikkinchi/', ikkinchi_page, name='ikkinchi_page'),
    path('kitob/3', buyuk_page, name='buyuk_page'),
    path('uchinchi/', uchinchi_page, name='uchinchi_page'),
]
