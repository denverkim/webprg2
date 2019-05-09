from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(
        max_length=200,
        help_text='Enter an article title'
    )
    body = models.TextField(
        max_length=1000,
        help_text='Enter an article'
    )
    author = models.CharField(
        max_length=200
    )
    create_date = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])
