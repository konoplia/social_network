import json
from http import HTTPStatus
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from blog.models import BlogPost, Reaction

User = get_user_model()


class GetLikesQuantityTests(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="example", password="example@123")
        self.blogpost = BlogPost.objects.create(user=self.user)
        self.reaction = Reaction.objects.create(blog_post=self.blogpost, user=self.user, like=True)
        self.url = reverse('analytics:like-counter-list')

    def test_get_likes_quantity(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class GetUserActivityTests(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="example", password="example@123")
        self.blogpost = BlogPost.objects.create(user=self.user)
        self.reaction = Reaction.objects.create(blog_post=self.blogpost, user=self.user, like=True)
        self.url = reverse('analytics:user-action-list')

    def test_get_user_activity(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
