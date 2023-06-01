from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from blog.models import Reaction

User = get_user_model()


class AnalyticSerializer(ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'


class UserLastLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username',
            'last_request',
            'last_jwt_login',
        ]
