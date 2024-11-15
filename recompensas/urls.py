from recompensas import views
from django.urls import path

urlpatterns = [
    path('', views.recompensas, name='recompensas'),
    path('resgatar', views.resgate_recompensas, name='resgate_recompensas'),
]
