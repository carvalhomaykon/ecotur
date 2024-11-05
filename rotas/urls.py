from rotas import views
from django.urls import path

urlpatterns = [
    path('', views.rotas, name='rotas'),
]
