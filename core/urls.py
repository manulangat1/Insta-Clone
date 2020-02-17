from django.urls import path
from .api import PictureAPI,PicturesAPI,CommentAPI,LikesAPI,LikeAPI

urlpatterns = [
    path('',PicturesAPI.as_view(),name="pictures"),
    path('feed/',PictureAPI.as_view(),name="picture"),
    path('comments/',CommentAPI.as_view(),name="comments"),
    path('likes/',LikeAPI.as_view(),name="likes"),
    path('likes/<pk>/',LikesAPI.as_view(),name="likes_detail"),
]