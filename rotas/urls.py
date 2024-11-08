from rotas import views
from django.urls import path

urlpatterns = [
    path('', views.rotas, name='rotas'),
    path('minha-rota/', views.minha_rota, name='minha_rota'),
    path('historico-rota', views.historico_rota, name='historico_rota'),
]
