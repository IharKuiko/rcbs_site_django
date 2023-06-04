from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Posts(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.CharField(max_length=256)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    create_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_published = models.BooleanField()
    image = models.ImageField()

