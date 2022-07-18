from django.db import models
from django.contrib.auth.models import User
from hotels.models import HotelProfile


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hotel_room')
    number = models.CharField(max_length=50)
    floor = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    isBooked = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.number


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.image