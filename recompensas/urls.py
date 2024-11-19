from recompensas import views
from django.urls import path

urlpatterns = [
    path('', views.recompensas, name='recompensas'),
    path('faca-login/', views.inicial_sem_login, name='inicial_sem_login'),
    path('resgatar', views.resgate_recompensas, name='resgate_recompensas'),
    path('detalhe-recompensa/<int:id>/', views.detalhe_recompensa, name='detalhe_recompensa'),
]
