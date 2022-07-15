from django.urls import path, include


urlpatterns = [
    path('hotels/', include('api.hotels.urls')),
    path('posts/', include('api.posts.urls')),
    path('rooms/', include('api.rooms.urls')),
]