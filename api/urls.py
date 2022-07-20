from django.urls import path, include


urlpatterns = [
    path('hotels/', include('api.hotels.urls')),
    path('rooms/', include('api.rooms.urls')),
    path('booking_room/', include('api.booking_room.urls'))
]