from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import *
from django.contrib.auth.hashers import make_password
from hotels.models import Hotel
from .serializers import *
from django.contrib.auth.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            data = super().validate(attrs)
            serializer = UserSerializerWithToken(self.user).data
            for k, v in serializer.items():
                data[k] = v
            return data
        except:
            raise ParseError({'detail':'Invalid username or password!!!'})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            username = data['username'],
            email=data['email'],
            password = make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        raise ParseError({'detail': 'Username is already exist!!!'})


class HotelView(APIView):

    def post(self, request):
        user = request.user
        data = request.data
        data['user'] = user.id
        serializer = HotelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request):
        user = request.user
        try:
            profile = Hotel.objects.get(user__id=user.id)
        except:
            return Response({'errors':'Profile does not exist'})
        serializer = HotelSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)