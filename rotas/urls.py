from rotas import views
from django.urls import path

urlpatterns = [
    path('', views.rotas, name='rotas'),
    path('minha-rota/', views.minha_rota, name='minha_rota'),
    path('historico-rota', views.historico_rota, name='historico_rota'),
    path('avaliar-rota', views.avaliar_rota, name='avaliar_rota'),
    path('adicionar-rota/', views.adicionar_rota, name='adicionar_rota'),
    path('salvar_historico_pontos/', views.salvar_historico_pontos, name='salvar_historico_pontos'),
]
