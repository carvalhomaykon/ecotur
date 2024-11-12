from pontos_turisticos import views
from django.urls import path

urlpatterns = [
    path('', views.pontos_turisticos, name='pontos_turisticos'),
    path('ponto-turistico/<int:id>/', views.detalhes_ponto_turistico, name='detalhes_ponto_turistico'),
]