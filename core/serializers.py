from .models import Picture,Comment


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
    class Meta:
        model = Picture
        fields = (
            'id',
            'image',
            'caption',
            'comments'
        )
    def get_comments(self,obj):
        return CommentSerializer(obj.comments.all(),many=True).data
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
        )