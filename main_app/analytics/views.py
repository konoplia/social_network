from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from blog.models import BlogPost
from analytics.serializers import AnalyticSerializer
# Create your views here


class LikesCounterView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = AnalyticSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['create_date',]

#     def get(self, request, *args, **kwargs):
#         print(self, request, args, kwargs, '--------------------')
#         return super().get(request, *args, **kwargs)
