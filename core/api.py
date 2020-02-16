from .models import Picture,Comment

from .serializers import PictureDetailsSerializer,PictureSerializer,CommentSerializer

from rest_framework import generics

class PicturesAPI(generics.ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureDetailsSerializer
class PictureAPI(generics.ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
class CommentAPI(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer