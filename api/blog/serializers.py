from rest_framework import serializers
from .models import User, BlogPost, RestrictBlogPost

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'password', 'profile_photo']
        extra_kwargs = {'password': {'write_only': True}}

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'profile_photo']

class BlogSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'author', 'author_name', 'content', 'create_at', 'update_at', 'draft']
        extra_kwargs = {'author': {'read_only': True}}

    def get_author_name(self, obj) -> str:
        return obj.author.name

class RestrictBlogSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = RestrictBlogPost
        fields = ['id', 'title', 'author', 'author_name', 'content', 'create_at', 'update_at', 'draft']
        extra_kwargs = {'author': {'read_only': True}}

    def get_author_name(self, obj) -> str:
        return obj.author.name

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']