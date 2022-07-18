from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from hotels.models import Country, HotelProfile, HotelImages
# from api.rooms.serializers import RoomSerializer


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class HotelProfileSerializer(serializers.ModelSerializer):
    # hotel_room = RoomSerializer(read_only=True, many=True)
    class Meta:
        model = HotelProfile
        fields = ['name', 'logo', 'country','city','address', 'phone','email','stars','description','user']


class HotelProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelProfile
        fields = ['user', 'name', 'country', 'city', 'stars', 'logo']


class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    isStaff = serializers.SerializerMethodField('get_isStaff')
    hotelProfile = HotelProfileSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'isAdmin', 'isStaff', 'hotelProfile']

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_isStaff(self, obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username','isAdmin', 'token', 'is_staff']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)