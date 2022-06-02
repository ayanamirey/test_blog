from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name="Title")
    text = models.TextField(verbose_name='Text')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Published Date')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец статьи', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Text')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Publish')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'self.text'
