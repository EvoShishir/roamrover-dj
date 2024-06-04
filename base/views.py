from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Location, LocationCost


# Create your views here.

class CategoriesList(ListView):
    model = Category


class LocationsList(ListView):
    model = Location


class SingleLocation(DetailView):
    model = Location


class LocationCosts(ListView):
    model = LocationCost
    context_object_name = "costs"
    template_name = "base/location_detail.html"
