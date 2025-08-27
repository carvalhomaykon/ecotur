from django.db import models

class Categoria(models.TextChoices):
    CULTURAL = "cultural", "Cultural"
    NATURAL = "natural", "Natural"
    SEM_CATEGORIA = "sem_categoria", "Sem Categoria"

class PontosTuristicos(models.Model):
    nome = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    descricao = models.TextField()
    categoria = models.CharField(max_length=20, choices=Categoria.choices, default=Categoria.SEM_CATEGORIA)

    cep = models.CharField(max_length=8)
    endereco = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

class ImagemPorPontoTuristico(models.Model):
    ponto_turistico = models.ForeignKey(PontosTuristicos, on_delete=models.CASCADE, related_name="imagens")
    imagem = models.ImageField(upload_to="pontos_turisticos/")

