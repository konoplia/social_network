from django.urls import path

from blog.views import ListCreatePostView, RetrieveUpdateDestroyPostView, PostLikeView, PostDisLikeView



app_name = 'blog'


urlpatterns = [
    path('post/', ListCreatePostView.as_view(), name='post-list-create'),
    path('post/<int:pk>/', RetrieveUpdateDestroyPostView.as_view(), name='post-retrieve-update-delete'),
    path('post/<int:pk>/like/', PostLikeView.as_view(), name='post-like'),
    path('post/<int:pk>/dis_like/', PostDisLikeView.as_view(), name='post-dislike'),
]
