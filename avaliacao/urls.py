from avaliacao import views
from django.urls import path

urlpatterns = [
    path('', views.avaliacao, name='avaliacao'),
]
