import json
from http import HTTPStatus
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from blog.models import BlogPost, Reaction

User = get_user_model()


class ListCreateBlogTests(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="example", password="example@123")
        self.blogpost = BlogPost.objects.create(user=self.user)
        self.url = reverse('blog:list-create-blogpost')
        self.data = {'content': 'some text'}

    def test_blog_post_create(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_get_blog_post(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class CreateReactionTests(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="example", password="example@123")
        self.blogpost = BlogPost.objects.create(user=self.user)
        self.another_blogpost = BlogPost.objects.create(user=self.user)
        self.reaction = Reaction.objects.create(blog_post=self.blogpost, user=self.user)
        self.url = reverse('blog:blogpost-reaction', kwargs={'pk': self.blogpost.id})
        self.url_for_another_blogpost = reverse('blog:blogpost-reaction', kwargs={'pk': self.another_blogpost.id})
        self.data = {'like': 'true'}

    def test_like_post_with_existing_object(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(self.url, data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_like_post_without_existing_object(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(self.url_for_another_blogpost, data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.CREATED)


class RetrieveUpdateDeleteBlogPostTests(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username="example", password="example@123")
        self.another_user = User.objects.create_user(username="example1", password="example@1231")
        self.blogpost = BlogPost.objects.create(user=self.user)
        self.another_blogpost = BlogPost.objects.create(user=self.another_user)
        self.url = reverse('blog:retrieve-update-delete-blogpost', kwargs={'pk': self.blogpost.id})
        self.url_for_another_blogpost = reverse('blog:retrieve-update-delete-blogpost', kwargs={'pk': self.another_blogpost.id})
        self.data = {'content': 'another post'}

    def test_get_your_blogpost(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_for_another_blogpost)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_update_your_blogpost(self):
        self.client.force_authenticate(user=self.another_user)
        response = self.client.patch(self.url_for_another_blogpost, data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_update_not_your_blogpost(self):
        self.client.force_authenticate(user=self.another_user)
        response = self.client.patch(self.url, data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)

    def test_delete_your_blogpost(self):
        self.client.force_authenticate(user=self.another_user)
        response = self.client.delete(self.url_for_another_blogpost)
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

    def test_delete_not_your_blogpost(self):
        self.client.force_authenticate(user=self.another_user)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)
