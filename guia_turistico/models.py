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

class IdiomaPorGuia(models.Model):
    class IdiomaChoices(models.TextChoices):
        PORTUGUES = "PT", "Português"
        INGLES = "EN", "Inglês"
        ESPANHOL = "ES", "Espanhol"
        FRANCES = "FR", "Francês"
        ALEMAO = "DE", "Alemão"

    guia = models.ForeignKey(GuiaTuristico, on_delete=models.CASCADE, related_name="idiomas")
    idioma = models.CharField(max_length=2, choices=IdiomaChoices.choices)

class RedeSocialPorGuia(models.Model):
    class TipoRede(models.TextChoices):
        INSTAGRAM = "instagram", "Instagram"
        FACEBOOK = "facebook", "Facebook"
        WHATSAPP = "whatsapp", "WhatsApp"
        TIKTOK = "tiktok", "TikTok"
        YOUTUBE = "youtube", "YouTube"

    guia = models.ForeignKey(GuiaTuristico, on_delete=models.CASCADE, related_name="redes")
    tipo = models.CharField(max_length=20, choices=TipoRede.choices)
    url = models.CharField(max_length=255)