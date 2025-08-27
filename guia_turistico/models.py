from django.db import models
from usuario.models import Users

# Create your models here.
class GuiaTuristico(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    senha = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    descricao = models.TextField()

class AvaliacaoGuia(models.Model):
    guia = models.ForeignKey(GuiaTuristico, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.CharField(max_length=200)
    data_avaliacao = models.DateTimeField(auto_now_add=True)