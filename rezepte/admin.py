from django.contrib import admin

# Register your models here.
from .models import Rezept

#class RezeptAdmin(admin.ModelAdmin):
#    list_display = ("bezeichnung", "koch", "kategorie",)

admin.site.register(Rezept)