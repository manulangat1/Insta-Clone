from .models import Picture,Comment,Likes

from .serializers import PictureDetailsSerializer,PictureSerializer,CommentsSerializer,LikeSerializer

from rest_framework import generics

class PicturesAPI(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureDetailsSerializer
class PictureAPI(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
class CommentAPI(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
class LikesAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
class LikeAPI(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer