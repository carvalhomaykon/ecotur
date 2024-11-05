from recompensas import views
from django.urls import path

urlpatterns = [
    path('', views.recompensas, name='recompensas'),
]
