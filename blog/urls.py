from django.urls import path

from blog.views import ListCreateBlogPostView, RetrieveUpdateDestroyBlogPostView, BlogPostReactionView


app_name = 'blog'


urlpatterns = [
    path('post/', ListCreateBlogPostView.as_view(), name='list-create-blogpost'),
    path('post/<int:pk>/',  RetrieveUpdateDestroyBlogPostView.as_view(), name='retrieve-update-delete-blogpost'),
    path('post/<int:pk>/reaction/', BlogPostReactionView.as_view(), name='blogpost-reaction'),
]
