import os
import json
from django.urls import reverse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_app.settings')
import django
from django.conf import settings

if not settings.configured:
    django.setup()
from faker import Faker
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
import random


NUMBER_OF_USER = 10
MAX_POSTS_PER_USER = 10
MAX_LIKES_PER_USER = 10

fake = Faker()
factory = APIRequestFactory()
client = APIClient()



def register_users():
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
    post_ids = []
    for token in tokens:
        for _ in range(random.randrange(0, MAX_POSTS_PER_USER)):
            response = client.post(reverse('blog:list-create-blogpost'), json.dumps({
                    'content': fake.sentence()
                    }), content_type='application/json', HTTP_AUTHORIZATION='Bearer '+ token)
            post_ids.append(response.json()['id'])
    return post_ids


def do_like_posts(posts_ids, tokens):
    for token in tokens:
        for _ in range(random.randrange(0, MAX_LIKES_PER_USER)):
            pk = random.choice(post_ids)
            response = client.patch(reverse('blog:blogpost-reaction', args=(pk,)), json.dumps({
                    'like': 'True'
                    }), content_type='application/json', HTTP_AUTHORIZATION='Bearer '+ token)
            post_ids.append(response.json()['id'])


fake_users = register_users()
fake_users_tokens = get_tokens(fake_users)
post_ids = create_posts(fake_users_tokens)
do_like_posts(post_ids, fake_users_tokens)
