from django.db import models
from pontos_turisticos.models import PontosTuristicos

# Create your models here.
class Users(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    nome_usuario = models.CharField(max_length=100)

class PontosVisitadosPorUser(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    ponto_turistico = models.ForeignKey(PontosTuristicos, on_delete=models.CASCADE)

    data = models.DateField()
    tempo_visita = models.IntegerField()
    nota = models.IntegerField()
    comentario = models.CharField(max_length=200)