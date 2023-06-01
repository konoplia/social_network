from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView

from blog.models import BlogPost, Reaction
from blog.serializers import BlogPostSerializer, ReactionSerializer

User = get_user_model()


class ListCreateBlogPostView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class RetrieveUpdateDestroyBlogPostView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostReactionView(UpdateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = ReactionSerializer
    queryset = BlogPost.objects.all()
    allowed_methods = ['PATCH', ]

    def get_object(self):
        return super().get_object()

    def update(self, request, *args, **kwargs):
        blog_post_obj = self.get_object()
        obj, created = Reaction.objects.get_or_create(
            user=User.objects.get(id=request.user.id),
            blog_post=blog_post_obj)

        reaction_data = request.data
        serializer = ReactionSerializer(instance=obj, data=reaction_data)
        
        if serializer.is_valid(raise_exception=True):
            reaction_instance = serializer.save()
        if created:
            return Response(ReactionSerializer(reaction_instance).data,
                                                    status=status.HTTP_201_CREATED)
        else:
            return Response(ReactionSerializer(reaction_instance).data,
                                                    status=status.HTTP_200_OK)
