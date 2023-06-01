from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(_("password"), max_length=128)
    last_jwt_login = models.DateTimeField(blank=True, null=True)
    last_request = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'username'
