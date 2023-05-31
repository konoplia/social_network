from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from blog.models import BlogPost


class AnalyticSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
