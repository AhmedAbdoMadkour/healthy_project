from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    publish_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.comment

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    like_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
