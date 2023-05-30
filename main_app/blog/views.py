from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView

from blog.models import Post
from blog.serializers import PostSerializer, RetrieveUpdateDestroyPostSerializer, PostLikeSerializer, PostDisLikeSerializer


class ListCreatePostView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class RetrieveUpdateDestroyPostView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Post.objects.all()
    serializer_class = RetrieveUpdateDestroyPostSerializer


class PostLikeView(UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = PostLikeSerializer
    queryset = Post.objects.all()
    allowed_methods = ['PATCH',]


class PostDisLikeView(UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = PostDisLikeSerializer
    queryset = Post.objects.all()
    allowed_methods = ['PATCH',]
