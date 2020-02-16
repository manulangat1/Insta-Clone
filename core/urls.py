from django.urls import path
from .api import PictureAPI,PicturesAPI,CommentAPI

urlpatterns = [
    path('',PicturesAPI.as_view(),name="pictures"),
    path('feed/',PictureAPI.as_view(),name="picture"),
    path('comments/',CommentAPI.as_view(),name="comments"),
]