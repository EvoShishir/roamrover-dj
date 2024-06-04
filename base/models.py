from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(
        upload_to="images/categories", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Location(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(
        upload_to="images/location", blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    overview = models.TextField(max_length=10000, blank=True, null=True)
    containsWater = models.BooleanField(default=False, blank=True, null=True)
    involveHiking = models.BooleanField(default=False, blank=True, null=True)
    acrophobic = models.BooleanField(default=False, blank=True, null=True)
    safe = models.BooleanField(default=False, blank=True, null=True)
    cautious = models.BooleanField(default=False, blank=True, null=True)
    unsafe = models.BooleanField(default=False, blank=True, null=True)
    iframe = models.CharField(max_length=10000, blank=True, null=True)
    lattitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class LocationCost(models.Model):
    location = models.ForeignKey(
        Location, related_name='costs', on_delete=models.CASCADE)
    cost_type = models.CharField(max_length=200, blank=True, null=True)
    cost = models.CharField(max_length=200, blank=True, null=True)
    distance = models.CharField(
        default="---", max_length=200, blank=True, null=True)
    time = models.CharField(
        default="---", max_length=200, blank=True, null=True)
    people = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.cost_type} - {self.cost}"
