from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name      

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    publish_confirm = models.BooleanField(default=False)
    
    post_image = models.ImageField(upload_to='fortune_board/images/%Y/%m/%d/', blank=True, null=True)    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/fortune_board/{self.pk}/'

