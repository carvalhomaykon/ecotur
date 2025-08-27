from django.db import models
from guia_turistico.models import GuiaTuristico
from pontos_turisticos.models import PontosTuristicos

# Create your models here.
class PacoteTuristico(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    contato = models.CharField(max_length=11)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

class GuiaPorPacote(models.Model):
    guia = models.ForeignKey(GuiaTuristico, on_delete=models.CASCADE)
    pacote = models.ForeignKey(PacoteTuristico, on_delete=models.CASCADE)

class PontosTuristicosPorPacote(models.Model):
    pacote = models.ForeignKey(PacoteTuristico, on_delete=models.CASCADE)
    ponto_turistico = models.ForeignKey(PontosTuristicos, on_delete=models.CASCADE)

class ImagemPorPacote(models.Model):
    pacote = models.ForeignKey(PacoteTuristico, on_delete=models.CASCADE, related_name="imagens")
    imagem = models.ImageField(upload_to="pacotes/")