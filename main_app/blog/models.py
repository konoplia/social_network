from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogPost(models.Model):

    id = models.AutoField(primary_key=True, blank=True)
    content = models.CharField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='posts')


class Reaction(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    like = models.BooleanField(default=False)
    like_date = models.DateField(blank=True, null=True)
    dislike = models.BooleanField(default=False)
    dislike_date = models.DateField(blank=True, null=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='reaction')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='reaction')
