from django.contrib import admin

# Register your models here.
from .models import Rezept, Speisenart, Kueche, Zutatenart

admin.site.register(Rezept)
admin.site.register(Speisenart)
admin.site.register(Kueche)
admin.site.register(Zutatenart)