from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, Post
from .serializers import UserSerializer, PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def create_user(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['get'])
    @cache_page(60 * 5)
    def retrieve_user(self, request, pk=None):
        user = self.get_object()
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @action(detail=True, methods=['put', 'patch'])
    def update_user(self, request, pk=None):
        user = self.get_object()
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    @action(detail=False, methods=['post'])
    def create_post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['get'])
    def retrieve_post(self, request, pk=None):
        post = self.get_object()
        serializer = PostSerializer(post)
        return Response(serializer.data)

    @action(detail=True, methods=['put', 'patch'])
    def update_post(self, request, pk=None):
        post = self.get_object()
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['delete'])
    def delete_post(self, request, pk=None):
        post = self.get_object()
        post.delete()
        return Response(status=204)

    @action(detail=False, methods=['get'])
    @cache_page(60 * 5)
    def list_posts(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
