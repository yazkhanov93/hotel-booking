from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class HotelProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.ImageField(default='logo.png')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    stars = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class HotelImages(models.Model):
    hotel = models.ForeignKey(HotelProfile, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.image