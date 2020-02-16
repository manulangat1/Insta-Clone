from .models import Picture,Comment,Likes


from rest_framework import serializers

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = (
            'id',
            'image',
            'caption'
        )
class PictureDetailsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    class Meta:
        model = Picture
        fields = (
            'id',
            'image',
            'caption',
            'comments',
            'likes'
        )
    def get_comments(self,obj):
        return CommentSerializer(obj.comments.all(),many=True).data
    def get_likes(self,obj):
        return LikesSerializer(obj.like.all(),many=True).data
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
        )
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'text',
        )
class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = (
            'id',
            'count',
            'downvotes',
        )
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = (
            'id',
            'count',
            'upvotes',
            'downvotes',
        )