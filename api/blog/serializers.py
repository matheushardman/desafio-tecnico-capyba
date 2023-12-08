from rest_framework import serializers
from .models import User, BlogPost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'password', 'profile_photo']
        extra_kwargs = {'password': {'write_only': True}, 'email': {'write_only': True}}

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'author', 'content', 'create_at', 'update_at', 'draft']