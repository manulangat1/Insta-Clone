from .models import Picture,Comment

from .serializers import PictureDetailsSerializer,PictureSerializer,CommentsSerializer

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