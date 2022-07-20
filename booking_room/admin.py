from django.contrib import admin
from .models import BookingRoom


@admin.register(BookingRoom)
class BookingRoomAdmin(admin.ModelAdmin):
    list_display = ['roomId', 'clientName', 'clientSurname', 'clientEmail', 'bookedFrom', 'bookedTo', 'checkIn']
    list_editable = ['checkIn',]