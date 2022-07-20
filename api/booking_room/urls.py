from django.urls import path
from . import views


urlpatterns = [
    path('booking-room/', views.BookingRoomView.as_view(), name='booking-room')
]