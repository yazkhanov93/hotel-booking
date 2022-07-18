from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from hotels.models import HotelProfile, HotelImages, Country
from rooms.models import Room
from .serializers import HotelProfileSerializer, UserSerializer, UserSerializerWithToken, CountrySerializer, HotelProfileListSerializer
from api.rooms.serializers import RoomSerializer


class CountryView(APIView):
    def get(self, request):
        try:
            country = Country.objects.all()
            serializer = CountrySerializer(country, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)

class MyTokenObtainSerializerView(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            data = super().validate(attrs)
            serializer = UserSerializerWithToken(self.user).data
            for k,v in serializer.items():
                data[k] = v
            return data
        except:
            raise ParseError({'detail':'Invalide username or password'})

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainSerializerView

@api_view(['POSt'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            username = data['username'],
            email = data['email'],
            password = make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except ValueError:
        return Response({'detail':'Username is already exist'})


class HotelProfileView(APIView):
    def post(self, request):
        user = request.user
        data = request.data
        # data['user'] = user.id
        serializer = HotelProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request,pk):
        try:
            hotel = HotelProfile.objects.get(id=pk)
            serializer = HotelProfileSerializer(hotel, many=False)
            rooms = Room.objects.filter(user=hotel.user)
            r_serializer = RoomSerializer(rooms, many=True)
            return Response({'hotel_detail':serializer.data, 'Hotel_rooms':r_serializer.data})
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)


class HotelProfileListView(APIView):
    def get(self, request):
        try:
            hotels = HotelProfile.objects.all()
            serializer = HotelProfileListSerializer(hotels, many=True)
            return Response(serializer.data)
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)