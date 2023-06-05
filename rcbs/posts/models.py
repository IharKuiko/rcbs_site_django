from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Posts(models.Model):
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
        ordering = ['-created_at']

    def __str__(self):
        return self.title

