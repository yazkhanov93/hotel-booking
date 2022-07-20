from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import BookingRoomSerializer
from booking_room.models import BookingRoom


class BookingRoomView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookingRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'detail':'room is booked'})