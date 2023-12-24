
from rest_framework import serializers
from .models import Post




class PostSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=100)
    # body = serializers.CharField(max_length=500)
    # slug = serializers.CharField(max_length=50)
    # publish = serializers.ChoiceField(choices=Post.Status.choices, default='d')


    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body', 'slug', 'publish', 'image', 'category', 'views']
