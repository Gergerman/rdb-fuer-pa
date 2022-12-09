from django.db import models

# Create your models here.
class Rezept(models.Model):
    koch = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    bezeichnung = models.CharField(max_length=80)
    kategorie = models.CharField(max_length=80)
    zutaten = models.TextField()
    zubereitung = models.TextField()

    def __str__(self):
        return self.bezeichnung