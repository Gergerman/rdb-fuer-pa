from django.urls import path
from .views import HomePageView, RezeptListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('liste/', RezeptListView.as_view(), name='list'),
]