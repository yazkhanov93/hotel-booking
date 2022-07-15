from django.contrib import admin
from .models import Hotel, Country


@admin.register(Country)
class CountrrryAdmin(admin.ModelAdmin):
    list_display = ['name',]



@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'city', 'address', 'phone', 'email', 'stars']