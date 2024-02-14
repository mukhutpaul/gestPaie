from django.db import models

class Frais(models.Model):
    codeFrais = models.CharField(max_length=10,primary_key=True)
    libelle = models.CharField(max_length=100)