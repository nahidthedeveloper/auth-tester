from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.manager import AccountManager


class Account(AbstractUser):
    first_name = None
    last_name = None

    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=150)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    objects = AccountManager()

    def __str__(self):
        return self.username
