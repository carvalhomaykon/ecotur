from recompensas import views
from django.urls import path

urlpatterns = [
    path('', views.recompensas, name='recompensas'),
    path('resgatar', views.regate_rescompensas, name='regate_rescompensas'),
]
