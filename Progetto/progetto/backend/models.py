from django.db import models

# Create your models here.
class Viaggi(models.Model):
    Titolo = models.CharField(max_length=64)
    Data =models.DateField(null=False)
    Descrizione = models.CharField(max_length=2000)
    Luogo = models.CharField(max_length=64)


    def __str__(self):
        return self.Titolo

    class Meta:
        ordering = ['Data']

