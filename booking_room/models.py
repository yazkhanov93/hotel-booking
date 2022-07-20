from django.db import models
from rooms.models import Room


class BookingRoom(models.Model):
    roomId = models.ForeignKey(Room, on_delete=models.CASCADE)
    clientEmail = models.EmailField(max_length=100)
    clientName = models.CharField(max_length=100)
    clientSurname = models.CharField(max_length=100)
    clientPassportCopy = models.FileField(null=True, blank=True)
    bookedFrom = models.DateField(auto_now_add=False)
    bookedTo = models.DateField(auto_now_add=False)
    checkIn = models.BooleanField(default=False)

    def __str__(self):
        return str(self.roomId.number)