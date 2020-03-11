from django.urls import path

from . import views

urlpatterns = [
    path('convertKml', views.convertKml, name='convertKml'),
    path('', views.index, name='index'),
]