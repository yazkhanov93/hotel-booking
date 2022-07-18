from django.urls import path
from . import views


urlpatterns = [
    path('category-list/', views.CategoryView.as_view(), name='category-list'),
    path('room-list/', views.RoomView.as_view(), name='room-list'),
    path('room-detail/<int:pk>/', views.RoomDetailView.as_view(), name='room-detail'),
]