from .api import UserListAPIView,UserProfileDetailView
from django.urls import path

urlpatterns = [
    path('',UserListAPIView.as_view(),name="user_list"),
    path('profile/<pk>/',UserProfileDetailView.as_view(),name="users_list"),
]