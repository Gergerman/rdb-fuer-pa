from django.db import models
from django.urls import reverse

# Create your models here.
#class Zutatenart(models.Model):
 #   name = models.CharField(max_length=80)

  #  class Meta:
   #     verbose_name_plural = "Art von Zutaten"

    #def __str__(self):
     #  return self.name

#class Kueche(models.Model):
#   name = models.CharField(max_length=80)

#   class Meta:
#        verbose_name_plural = "Küchen"

#    def __str__(self):
##       return self.name

#class Speisenart(models.Model):
#    name = models.CharField(max_length=80)

#    class Meta:
#        verbose_name_plural = "Speisenarten"

#    def __str__(self):
#       return self.name

SPEISENART = [
    ('Vorspeise, Zwischengericht','Vorspeise, Zwischengericht'),
    ('Suppe, Suppeneinlage', 'Suppe, Suppeneinlage'),
    ('Hauptspeise','Hauptspeise'),
    ('Beilage','Beilage'),
    ('Salat','Salat'),
    ('Nachspeise','Nachspeise'),
    ('Brot, Gebäck','Brot, Gebäck'),
    ('Sauce, Dipp','Sauce, Dipp'),
    ('Torte, Kuchen','Torte, Kuchen'),
    ('Kekse','Kekse')
    ]

KUECHE = [
    ('international','international'),
    ('österreichisch','österreichisch'),
    ('italienisch','italienisch'),
    ('britisch','britisch'),
    ('thailändisch','thailändisch'),
    ('chinesisch','chinesisch'),
    ('französisch','französisch'),
    ('spanisch','spanisch'),
    ('japanisch','japanisch'),
    ('georgisch','georgisch'),
    ('levantinisch','levantinisch'),
    ('---------','---------')
    ]

ZUTATART = [
    ('Fleisch','Fleisch'),
    ('Schwein','Schwein'),
    ('Rind','Rind'),
    ('Lamm','Lamm'),
    ('Huhn, Geflügel','Huhn, Geflügel'),
    ('Wild','Wild'),
    ('Pasta','Pasta'),
    ('Gemüse','Gemüse'),
    ('Obst','Obst'),
    ('Reis, Getreide','Reis, Getreide'),
    ('Mehlspeise','Mehlspeise'),
    ('Fisch, Meeresfrüchte','Fisch, Meeresfrüchte'),
    ('-----','-----------')
]

class Rezept(models.Model):
    koch = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    bezeichnung = models.CharField(max_length=120)
    kategorie = models.CharField(max_length=80, choices=SPEISENART)
    #kategorie = models.ForeignKey(Speisenart, on_delete=models.CASCADE)
    #kueche = models.ForeignKey(Kueche, on_delete=models.CASCADE)
    kueche = models.CharField(max_length=80, blank=True, choices=KUECHE)
    #art_zutaten = models.ForeignKey(Zutatenart, on_delete=models.CASCADE)
    art_zutaten = models.CharField(max_length=80, blank=True, choices=ZUTATART)
    vegetarisch = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    portionen = models.PositiveIntegerField(blank=True, null=True, default=4)
    bewertung = models.PositiveIntegerField(blank=True, null=True)
    zutaten = models.TextField()
    zubereitung = models.TextField(blank=True)
    anmerkungen = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "rezepte"

    def __str__(self):
        return self.bezeichnung

    def get_absolute_url(self):
        return reverse('redetail', args=[str(self.id)])