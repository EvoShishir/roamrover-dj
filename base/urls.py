from django.urls import path

from .views import CategoriesList, LocationsList, SingleLocation, CategoryLocationList

urlpatterns = [
    path("", CategoriesList.as_view(), name="categories"),
    path("locations", LocationsList.as_view(), name="locations"),
    path("locations/<int:pk>/", SingleLocation.as_view(), name="location"),
    path("categories/<int:category_id>/locations/",
         CategoryLocationList.as_view(), name="category_locations"),
]
