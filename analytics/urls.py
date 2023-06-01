from django.urls import path

from analytics.views import LikesCounterView, UserLastLoginView

app_name = 'analytics'


urlpatterns = [
    path('likes_counter/', LikesCounterView.as_view(), name='like-counter-list'),
    path('user_actions/', UserLastLoginView.as_view(), name='user-action-list'),
]
