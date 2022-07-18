from django.contrib import admin
from .models import Category, Room, RoomImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title',]


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number', 'user', 'floor', 'price', 'category', 'isBooked']
    list_editable = ['isBooked',]