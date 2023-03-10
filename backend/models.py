from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ViaggiFatti(models.Model):
    Titolo = models.CharField(max_length=64, blank=False)
    Data =models.DateField(blank=False)
    Descrizione = models.CharField(max_length=2000, blank=True, default="Nessuna Descrizione")
    Luogo = models.CharField(max_length=64, blank=False)
    Autore = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Titolo
        
    class Meta: 
        ordering = ['Data']

class ViaggiDaFare(models.Model):
    Titolo = models.CharField(max_length=64, blank=False)
    Data =models.DateField(blank=False)
    Attivita = models.CharField(max_length=2000, blank=True, default="Nessuna Attività Da Svolgere")
    Luogo = models.CharField(max_length=64, blank=False)
    Autore = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Titolo
        
    class Meta: 
        ordering = ['Data']

