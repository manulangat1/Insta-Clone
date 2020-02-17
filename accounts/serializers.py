from . models import Profile,FriendRequest

from rest_framework import serializers
from django.contrib.auth.models import User
class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self,value):
        return value
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email'
        )
class ProfileSerializer(serializers.ModelSerializer):
    user = StringSerializer()
    # friends = StringSerializer()
    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'slug',
            'friends',
        )
class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = (
            'id',
            'from_user',
            'to_user',
            'timestamp'
        )