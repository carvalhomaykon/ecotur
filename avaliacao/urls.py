from avaliacao import views
from django.urls import path

urlpatterns = [
    path('', views.avaliacao_geral, name='avaliacao_geral'),
]
