from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('guia-turistico/', include('guia_turistico.urls')),
    path('recompensas/', include('recompensas.urls')),
    path('rotas/', include('rotas.urls')),
    path('pontos-turisticos/', include('pontos_turisticos.urls')),
    path('avaliacao/', include('avaliacao.urls')),
    path('usuario/', include('usuario.urls')),
]