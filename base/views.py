from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Location, LocationCost


# Create your views here.

class CategoriesList(ListView):
    model = Category


class CategoryLocationList(ListView):
    model = Location
    template_name = 'location_list.html'
    context_object_name = 'locations'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category = get_object_or_404(Category, id=category_id)
        return Location.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category, id=self.kwargs['category_id'])
        return context


class LocationsList(ListView):
    model = Location


class SingleLocation(DetailView):
    model = Location

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['costs'] = LocationCost.objects.filter(location=self.object)
        # Fetch the city name of the current location
        city_name = self.object.city
        # Get all locations with the same city name, excluding the current location
        context['nearbyLocations'] = Location.objects.filter(
            city=city_name).exclude(pk=self.object.pk)
        return context
