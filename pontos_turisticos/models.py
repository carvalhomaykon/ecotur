from django.db import models

# Create your models here.
class PontosTuristicos(models.Model):
    nome = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    descricao = models.TextField()

    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)