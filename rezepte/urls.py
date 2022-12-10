from django.urls import path
from .views import HomePageView, RezeptListView, RezeptDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('liste/', RezeptListView.as_view(), name='list'),
    path('rezept/<int:pk>/', RezeptDetailView.as_view(), name='redetail'),
]