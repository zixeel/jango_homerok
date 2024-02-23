from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='mail')

    phone = models.CharField(max_length=35, verbose_name='phone number', editable=True, **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', editable=True, **NULLABLE)
    country = models.CharField(max_length=35, verbose_name='country', **NULLABLE)
    token = models.CharField(max_length=32, verbose_name='Token', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
