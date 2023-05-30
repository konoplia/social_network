from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):

    id = models.AutoField(primary_key=True, blank=True)
    content = models.CharField(max_length=2000)
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(User, related_name='post_likes')
    # like_date = models.DateField(auto_now=True, blank=True, null=True)
    dis_likes = models.ManyToManyField(User, related_name='post_dis_likes')
    # dis_like_date = models.DateField(auto_now=True, blank=True, null=True)
