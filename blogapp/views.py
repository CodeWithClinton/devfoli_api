from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import UserRegistrationSerializer, BlogSerializer, UserInfoSerializer
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()  # Save the user
        return Response({'id': user.id, 'username': user.username}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def blog_list(request):
#     blogs = Blog.objects.all()
#     serializer = BlogSerializer(blogs, many=True)
#     return Response(serializer.data)


class BlogPagination(PageNumberPagination):
    page_size = 6  # Number of results per page

@api_view(['GET'])
def blog_list(request):
    blogs = Blog.objects.all()
    paginator = BlogPagination()
    paginated_blogs = paginator.paginate_queryset(blogs, request)
    serializer = BlogSerializer(paginated_blogs, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
    user = request.user 
    
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_blog(request, slug):
    user = request.user 
    blog = Blog.objects.get(slug=slug)
    if blog.author != user:
        return Response({"error": "You are not the author of this blog"}, status=403)
    serializer = BlogSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_blog(request, slug):
    user = request.user 
    blog = Blog.objects.get(slug=slug)
    if blog.author != user:
        return Response({"error": "You are not the author of this blog"}, status=403)
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    

# new added section
@api_view(['GET'])
def user_info(request, username):
    User = get_user_model()
    user = User.objects.get(username=username)
    serializer = UserInfoSerializer(user)
    return Response(serializer.data)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_username(request):
    user = request.user 
    return Response({"username": user.username})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user 
    serializer = UserInfoSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)