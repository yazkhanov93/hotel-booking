from django.contrib import admin
from .models import Country, HotelProfile, HotelImages


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(HotelProfile)
class HotelProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'country','city','address', 'phone','email','stars']


@admin.register(HotelImages)
class HotelImageAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'image']