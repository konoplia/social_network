from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

from blog.models import Reaction
from analytics.serializers import AnalyticSerializer, UserLastLoginSerializer
from analytics.filters import FilterByLikeDate


User = get_user_model()


class LikesCounterView(ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = AnalyticSerializer
    filterset_class = FilterByLikeDate

    def get_queryset(self):
        queryset = Reaction.objects.filter(like=True)
        return queryset


class UserLastLoginView(ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserLastLoginSerializer
    queryset = User.objects
    