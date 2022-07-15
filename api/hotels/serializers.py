from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from hotels.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    isStaff = serializers.SerializerMethodField('get_isStaff')
    hotel = HotelSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'isAdmin', 'hotel', 'isStaff']
    
    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_isStaff(self, obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username','isAdmin','token','is_staff']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)