from . models import Profile,FriendRequest
from .serializers import ProfileSerializer,FriendRequestSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
class UserListAPIView(generics.ListCreateAPIView):
    # queryset = Profile.objects.exclude(user=request.user)
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        user = self.request.user
        slug = user
        serializer.save(user=user,slug=slug)
    def get_queryset(self):
        user = self.request.user
        return Profile.objects.exclude(user=user)
class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
class ListUnseenFriendRequests(APIView):
    serializer_class = FriendRequestSerializer
    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.data['to_user'])
        print(user)                              
        frequest,created = FriendRequest.objects.get_or_create(
            from_user = request.user,
            to_user = user
        )
        return Response({'status': 'Request sent'}, status=201)
class DeleteFriendRequest(APIView):
    serializer_class = FriendRequestSerializer
    def post(self,request,*args,**kwargs):
        user = User.objects.get(pk=request.data['to_user'])
        print(user) 
        frequest = FriendRequest.objects.filter(
            from_user = request.user,
            to_user = user
        ).first()
        frequest.delete()
        print(frequest)
        return Response({"deleted"})
class AcceptFriendRequest(APIView):
    serializer_class = FriendRequestSerializer
    def post(self,request,*args,**kwargs):
        user = User.objects.get(pk=request.data['from_user'])
        users = User.objects.get(pk=request.data['to_user'])
        frequest = FriendRequest.objects.filter(
            from_user = user,
            to_user = users
        ).first()
        print(users)
        user.profile.friends.add(users.profile)
        users.profile.friends.add(user.profile)
        frequest.delete()
        return Response({"deleted"})
# class 