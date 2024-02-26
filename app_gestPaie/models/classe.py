from django.db import models

class Classe(models.Model):
    codeclass = models.CharField(max_length=10,primary_key=True)
    libelleclass = models.CharField(max_length=100)