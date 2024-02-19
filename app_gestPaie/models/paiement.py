from django.db import models

class paiment(models.Model):
    codeFrais = models.CharField(max_length=10,primary_key=True)
    datepaie = models.CharField(max_length=20)
    montant = models.CharField(max_length=10)