from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50, null=False, unique=True)
    image = models.ImageField(verbose_name='Image', null=True, blank=True)
    description = models.CharField(verbose_name='Description', max_length=200, null=False, default='')
    created = models.DateTimeField(verbose_name='Created', auto_now=True, null=False)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=False, null=True, blank=True)

    category_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Article(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100, null=False, unique=True)
    description = models.CharField(max_length=200, verbose_name='Description', null=False, default='')
    content = models.TextField(verbose_name='Content', null=False)
    image = models.ImageField(verbose_name='Image', null=True, blank=True)
    created = models.DateTimeField(verbose_name='Created', auto_now=True, null=False)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=False, null=True, blank=True)
    publication_date = models.DateField(verbose_name='Publicated', auto_now=False, null=True)
    visible = models.BooleanField(default=False)

    article_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    article_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.content


class Tag(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50, null=False, unique=True)
    created = models.DateTimeField(verbose_name='Created', auto_now=True, null=False)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=False, null=True, blank=True)

    tag_article = models.ManyToManyField(Article, db_table='tag__article')

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name='Comment', max_length=1000, null=False)
    created = models.DateTimeField(verbose_name='Created', auto_now=True, null=False)

    comment_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comment_article = models.ForeignKey(Article, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.content
