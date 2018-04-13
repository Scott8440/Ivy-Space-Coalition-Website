from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    logo = models.ImageField(upload_to='organization_logos/')
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

