from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    customer_id = models.CharField(max_length=10)
    birth_day = models.DateField(null=True, blank=True)
    birth_time = models.TimeField(null=True, blank=True)
