from django.db import models
from app_gestPaie.models.frais import *
from app_gestPaie.models.eleve import *

class paiment(models.Model):
    codeFrais = models.ForeignKey(Frais,on_delete=models.CASCADE)
    eleve = models.ForeignKey(Eleve,on_delete=models.CASCADE)
    datepaie = models.CharField(max_length=20)
    montant = models.CharField(max_length=10)