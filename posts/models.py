from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    category = models.ManyToManyField('Category')

    def published_in_past(self):
        now = timezone.now()
        return self.pub_date <= now
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=(self.slug))


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_category', args=(self.slug))
