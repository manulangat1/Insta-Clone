from .api import UserListAPIView,UserProfileDetailView,ListUnseenFriendRequests,DeleteFriendRequest,AcceptFriendRequest
from django.urls import path

urlpatterns = [
    path('',UserListAPIView.as_view(),name="user_list"),
    path('f/',ListUnseenFriendRequests.as_view(),name="friends_list"),
    path('f/d/',DeleteFriendRequest.as_view(),name="friends_delete"),
    path('f/a/',AcceptFriendRequest.as_view(),name="friends_accept"),
    path('profile/<pk>/',UserProfileDetailView.as_view(),name="users_list"),
]