from guia_turistico import views
from django.urls import path

urlpatterns = [
    path('', views.guia_turistico, name='guia_turistico'),
]
