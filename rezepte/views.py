from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Rezept

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class RezeptListView(ListView):
    model = Rezept
    template_name = 'list.html'