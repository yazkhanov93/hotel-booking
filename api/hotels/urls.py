from django.urls import path
from .import views


urlpatterns = [
    path('country-list/', views.CountryView.as_view(), name='country-list'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('create-hotel/', views.HotelProfileView.as_view(), name='create-hotel'),
]