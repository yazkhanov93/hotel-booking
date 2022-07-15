from django.db import models
from hotels.models import Hotel


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Room(models.Model):
    number = models.CharField(max_length=255, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    floor = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    isBooked = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.number


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField()