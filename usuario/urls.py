# urls.py
from usuario import views
from django.urls import path

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.user_logout, name='logout'),  # Altere para views.user_logout
]
