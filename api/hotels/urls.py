from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('hotel-list/', views.HotelView.as_view(), name='hotel_list'),
    path('create_hotel/', views.HotelView.as_view(), name='create_hotel')
]