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
    ('Suppe', 'Suppe'),
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
    ('österreichisch','österreichisch'),
    ('italienisch','italienisch'),
    ('thailändisch','thailändisch'),
    ('chinesisch','chinesisch'),
    ('französisch','französisch')
    ]

ZUTATART = [
    ('Fleisch','Fleisch'),
    ('Fleisch - Schwein','Fleisch - Schwein'),
    ('Fleisch - Rind','Fleisch - Rind'),
    ('Fleisch - Lamm','Fleisch - Lamm'),
    ('Fleisch - Huhn, Geflügel','Fleisch - Huhn, Geflügel'),
    ('Fleisch - Wild','Fleisch - Wild'),
    ('Pasta','Pasta'),
    ('vegetarisch','vegetarisch'),
    ('vegetarisch - Pasta','vegetarisch - Pasta'),
    ('vegetarisch - Gemüse','vegetarisch - Gemüse'),
    ('vegetarisch - Mehlspeise','vegetarisch - Mehlspeise'),
    ('Fisch, Meeresfrüchte','Fisch, Meeresfrüchte')
]

class Rezept(models.Model):
    koch = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    bezeichnung = models.CharField(max_length=80)
    kategorie = models.CharField(max_length=80, choices=SPEISENART)
    #kategorie = models.ForeignKey(Speisenart, on_delete=models.CASCADE)
    #kueche = models.ForeignKey(Kueche, on_delete=models.CASCADE)
    kueche = models.CharField(max_length=80, blank=True, choices=KUECHE)
    #art_zutaten = models.ForeignKey(Zutatenart, on_delete=models.CASCADE)
    art_zutaten = models.CharField(max_length=80, blank=True, choices=ZUTATART)
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