from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Rezept
from django.db.models import Q

# Create your views here.
class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

class RezeptListView(LoginRequiredMixin,ListView):
    model = Rezept
    template_name = 'list.html'
    context_object_name = 'suchergebnis'

    def get_queryset(self):
        q1 = self.request.GET.get("SF1")
        q2 = self.request.GET.get("SF2")
        veget = self.request.GET.get("vegetarisch")
        vegan = self.request.GET.get("vegan")
        eigen = self.request.GET.get("eigen")

        veganliste=Rezept.objects.filter(vegan=True)
        vegetliste=Rezept.objects.filter(vegetarisch=True)

        rezeptliste1 = (Rezept.objects.filter(Q(bezeichnung__icontains=q1) 
        | Q(kategorie__icontains=q1)
        | Q(kueche__icontains=q1) 
        | Q(art_zutaten__icontains=q1)))

        rezeptliste2 = (Rezept.objects.filter(Q(bezeichnung__icontains=q2) 
        | Q(kategorie__icontains=q2)
        | Q(kueche__icontains=q2) 
        | Q(art_zutaten__icontains=q2))
        .order_by('bezeichnung'))

        if vegan:
            suchergebnis = rezeptliste1 & rezeptliste2 & veganliste
        elif veget:
            suchergebnis = rezeptliste1 & rezeptliste2 & (vegetliste | veganliste)
        else:
            suchergebnis = rezeptliste1 & rezeptliste2
        if eigen:
            suchergebnis = suchergebnis.filter(koch=self.request.user)
        return suchergebnis

class RezeptDetailView(LoginRequiredMixin,DetailView):
    model = Rezept
    template_name = 'redetail.html'

class RezeptNeuView(LoginRequiredMixin,CreateView):
    model = Rezept
    template_name = 'reneu.html'
    fields = ['bezeichnung', 'kategorie', 'kueche', 'art_zutaten', 'vegetarisch', 'vegan', 'portionen', 'zutaten', 'zubereitung', 'anmerkungen']

    def form_valid(self, form):
        form.instance.koch = self.request.user
        return super().form_valid(form)

class RezeptUpdateView(UserPassesTestMixin, UpdateView):
    model = Rezept
    template_name = 'reedit.html'
    fields = ['bezeichnung', 'kategorie', 'kueche', 'art_zutaten', 'vegetarisch', 'vegan', 'portionen', 'zutaten', 'zubereitung', 'anmerkungen']

    def test_func(self):
        obj = self.get_object()
        return obj.koch == self.request.user

class RezeptDeleteView(UserPassesTestMixin, DeleteView):
    model = Rezept
    template_name = 'redelete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.koch == self.request.user

    


