from rest_framework import serializers
from .models import Blog, CustomUser
from django.contrib.auth import get_user_model


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', "first_name", "last_name", 'password']  # Keep it simple
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure password is write-only
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user


class VerySimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "first_name", "last_name", "profile_picture"]



class BlogSerializer(serializers.ModelSerializer):
    author = VerySimpleUserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'author', 'category', 'content', 'featured_image', 'published_date', 'created_at', 'updated_at', 'is_draft']



class UserInfoSerializer(serializers.ModelSerializer):
    blog_posts = serializers.SerializerMethodField()
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name", "job_title", "bio", "profile_picture", "facebook", "twitter", "instagram", "linkedin", "blog_posts"]

    
    def get_blog_posts(self, user):
        blogs = user.blog_posts.all()[:9]
        serializer = BlogSerializer(blogs, many=True)
        return serializer.data