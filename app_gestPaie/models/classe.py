from django.db import models

class classe(models.Model):
    codeclass = models.CharField(max_length=10,primary_key=True)
    libelleclass = models.CharField(max_length=100)