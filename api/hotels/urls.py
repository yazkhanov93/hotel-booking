from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('create_profile/', views.HotelView.as_view(), name='create_profile')
]