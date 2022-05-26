from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name="Title")
    text = models.TextField(verbose_name='Text')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Published Date')
    published = models.BooleanField(default=False, verbose_name="Published")

    def __str__(self):
        return f'{self.title}'
