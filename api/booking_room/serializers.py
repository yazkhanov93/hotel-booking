from rest_framework import serializers
from booking_room.models import BookingRoom


class BookingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingRoom
        fields = '__all__'

    