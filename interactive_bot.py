import os
import json
import random
import django

from faker import Faker
from django.urls import reverse
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_app.settings')

if not settings.configured:
    django.setup()

from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from main_app.settings import NUMBER_OF_USER, MAX_POSTS_PER_USER, MAX_LIKES_PER_USER


fake = Faker()
factory = APIRequestFactory()
client = APIClient()


def register_users():
    """
    functions whic creating and register users in app
    """
    fake_users = {}
    for _ in range(NUMBER_OF_USER):
        user_name = fake.first_name()
        password = fake.password()
        email = fake.email()
        fake_users.update({_: [user_name, password, email]})
        response = client.post(reverse('authentication:register'), json.dumps({
        'username': user_name, 'password': password, 'email': email
        }), content_type='application/json')
    return fake_users


def get_tokens(fake_users):
    """
    get jwt tokens
    """
    fake_user_tokens = []
    for user in fake_users.values():
        try:
            response = client.post(reverse('authentication:token_obtain_pair'), json.dumps({
                    'username': user[0], 'password': user[1]
                    }), content_type='application/json')
            fake_user_tokens.append(response.json()['access'])
        except KeyError:
            pass
    return fake_user_tokens


def create_posts(tokens):
    """
    creating random quantity of posts
    """
    post_ids = []
    for token in tokens:
        for _ in range(random.randrange(0, MAX_POSTS_PER_USER)):
            response = client.post(reverse('blog:list-create-blogpost'), json.dumps({
                    'content': fake.sentence()
                    }), content_type='application/json', HTTP_AUTHORIZATION='Bearer '+ token)
            post_ids.append(response.json()['id'])
    return post_ids


def do_like_posts(posts_ids, tokens):
    """
    like random post
    every user do random quantity likes
    """
    for token in tokens:
        for _ in range(random.randrange(0, MAX_LIKES_PER_USER)):
            pk = random.choice(post_ids)
            try:
                response = client.patch(reverse('blog:blogpost-reaction', args=(pk,)), json.dumps({
                        'like': 'True'
                        }), content_type='application/json', HTTP_AUTHORIZATION='Bearer '+ token)
                post_ids.append(response.json()['id'])
            except KeyError:
                pass


fake_users = register_users()
fake_users_tokens = get_tokens(fake_users)
post_ids = create_posts(fake_users_tokens)
do_like_posts(post_ids, fake_users_tokens)

print(f'Created {len(fake_users)} users')
print(f'Created {len(post_ids)} posts')
