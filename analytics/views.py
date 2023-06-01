from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

from blog.models import Reaction
from analytics.serializers import AnalyticSerializer, UserLastLoginSerializer
from analytics.filters import FilterByLikeDate
from rest_framework.response import Response


User = get_user_model()


class LikesCounterView(ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = AnalyticSerializer
    filterset_class = FilterByLikeDate

    def get_queryset(self):
        queryset = Reaction.objects.filter(like=True)
        return queryset

    def list(self, request, *args, **kwargs):
        gte = request.query_params.get('like_date__gte')
        lte = request.query_params.get('like_date__lte')
        if gte and lte:
            filter = Q(like_date__gte=gte) & Q(like_date__lte=lte)
        elif gte and lte is None:
            filter = Q(like_date__gte=gte)
        elif lte and gte is None:
            filter = Q(like_date__lte=lte)
        else:
            filter = Q()
        queryset = self.get_queryset()
        queryset = queryset.filter(filter)

        return Response({"count": queryset.count()})


class UserLastLoginView(ListAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = UserLastLoginSerializer
    queryset = User.objects
    