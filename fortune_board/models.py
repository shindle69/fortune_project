from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField()
    publish_confirm = models.BooleanField(default=False)
    
    post_image = models.ImageField(upload_to='fortune_board/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return (self.title)

    def get_absolute_url(self):
        return f'/fortune_board/{self.pk}/'
        
    

