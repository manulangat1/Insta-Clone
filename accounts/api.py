from . models import Profile,FriendRequest
from .serializers import ProfileSerializer
from rest_framework import generics
class UserListAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer