from django.urls import path, include


urlpatterns = [
    path('hotels/', include('api.hotels.urls')),
    path('rooms/', include('api.rooms.urls')),
]