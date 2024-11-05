from pontos_turisticos import views
from django.urls import path

urlpatterns = [
    path('', views.pontos_turisticos, name='pontos_turisticos'),
    path('historia_curiosidades/', views.historia_pt, name='hisoria_pt'),
]
