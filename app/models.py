from django.db import models

# Create your models here.

class Filmes(models.Model):
    nome = models.CharField(max_length=150)
    data = models.DateField(max_length=100)
    autor = models.CharField(max_length=100)
