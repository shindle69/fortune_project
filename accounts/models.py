from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    nick_name = models.CharField(max_length=10)
    birth_day = models.DateField(null=True, blank=True)
    birth_time = models.TimeField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
      return f'{self.nick_name} Profile'
