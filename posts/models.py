from django.db import models
from hotels.models import Hotel


class Post(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField()