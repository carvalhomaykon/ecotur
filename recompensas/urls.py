from recompensas import views
from django.urls import path

urlpatterns = [
    path('', views.recompensas, name='recompensas'),
    path('resgatar', views.resgate_recompensas, name='resgate_recompensas'),
    path('detalhe-recompensa/<int:id>/', views.detalhe_recompensa, name='detalhe_recompensa'),
]
