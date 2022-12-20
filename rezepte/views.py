from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Rezept
from django.db.models import Q

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class RezeptListView(ListView):
    model = Rezept
    template_name = 'list.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Rezept.objects.filter(bezeichnung__icontains=query).order_by('bezeichnung')
        return object_list

class RezeptDetailView(DetailView):
    model = Rezept
    template_name = 'redetail.html'

class RezeptNeuView(CreateView):
    model = Rezept
    template_name = 'reneu.html'
    fields = ['bezeichnung', 'kategorie', 'kueche', 'art_zutaten', 'portionen', 'zutaten', 'zubereitung']

    def form_valid(self, form):
        form.instance.koch = self.request.user
        return super().form_valid(form)
