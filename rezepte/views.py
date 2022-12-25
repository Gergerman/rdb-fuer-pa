from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class RezeptNeuView(LoginRequiredMixin,CreateView):
    model = Rezept
    template_name = 'reneu.html'
    fields = ['bezeichnung', 'kategorie', 'kueche', 'art_zutaten', 'portionen', 'zutaten', 'zubereitung', 'anmerkungen']

    def form_valid(self, form):
        form.instance.koch = self.request.user
        return super().form_valid(form)

class RezeptUpdateView(UserPassesTestMixin, UpdateView):
    model = Rezept
    template_name = 'reedit.html'
    fields = ['bezeichnung', 'kategorie', 'kueche', 'art_zutaten', 'portionen', 'zutaten', 'zubereitung', 'anmerkungen']

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

    


