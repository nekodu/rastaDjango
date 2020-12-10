
from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name="anasayfa"),
    path('randevu', views.randevu, name="randevu"),
]