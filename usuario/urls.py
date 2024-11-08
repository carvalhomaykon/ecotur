from usuario import views
from django.urls import path

urlpatterns = [
    path('', views.usuario, name='usuario'),
    path('cadastro/', views.cadastro, name='cadastro'),

]
