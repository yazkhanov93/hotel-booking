from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(default='Group_28.png')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    stars = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

        
