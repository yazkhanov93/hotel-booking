from rest_framework import serializers
from django.contrib.auth.models import User
from rooms.models import Category, Room, RoomImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'