from django.contrib import admin

# Register your models here.
from .models import Rezept, Speisenart

#class RezeptAdmin(admin.ModelAdmin):
#    list_display = ("bezeichnung", "koch", "kategorie",)

admin.site.register(Rezept)
admin.site.register(Speisenart)