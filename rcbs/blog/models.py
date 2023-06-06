from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    description = models.CharField(max_length=256, verbose_name='Описание')
    content = models.TextField(verbose_name='Текст статьи')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Созданно')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Измененно')
    is_published = models.BooleanField(verbose_name='Опубликованно')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})
