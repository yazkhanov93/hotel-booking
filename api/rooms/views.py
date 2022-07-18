from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rooms.models import Room,RoomImage,Category
from .serializers import CategorySerializer, RoomSerializer


class CategoryView(APIView):
    def get(self, request):
        try:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RoomView(APIView):
    def get(self, request):
        try:
            room = Room.objects.all()
            serializer = RoomSerializer(room, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(serlf,request):
        data = request.data
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class RoomDetailView(APIView):
    def get(self, request, pk):
        try:
            room = Room.objects.get(id=pk)
            serializer = RoomSerializer(room, many=False)
            return Response(serializer.data)
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)