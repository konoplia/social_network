from django.urls import path
from analytics.views import LikesCounterView

# from blog.views import ListCreatePostView, RetrieveUpdateDestroyPostView, PostLikeView, PostDisLikeView

app_name = 'analytics'


urlpatterns = [
    path('likes_counter/', LikesCounterView.as_view(), name='like-counter-list'),
]
