from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from blog.models import Post


class AnalyticSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'