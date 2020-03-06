# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from slugify import slugify
from autoslug import AutoSlugField
from taggit.managers import TaggableManager


# Create your models here.


class Category(models.Model):
    name = models.CharField("نام", max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'پیش نویس'),
        ('published', 'منتشر شده')
    )

    title = models.CharField("عنوان", max_length=250, unique=True)
    abstract = models.CharField("خلاصه", max_length=100)
    slug = AutoSlugField(populate_from='title', allow_unicode=True)
    author = models.ForeignKey(User, related_name="Author_Post", on_delete=models.CASCADE)
    body = models.TextField("متن")
    defaultImage = models.ImageField("عکس پیش فرض", upload_to="img/News", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = TaggableManager()
    created = models.DateTimeField("تاریخ انتشار", auto_now_add=True)
    updated = models.DateTimeField("تاریخ ویرایش", auto_now_add=True)
    status = models.CharField("وضعیت", max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:details', args=[self.slug])


class PhotoPost(models.Model):
    name = models.CharField("نام", max_length=200)
    address = models.ImageField(upload_to='img/post/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField("متن", )
    email = models.EmailField("ایمیل", )
    created = models.DateTimeField("تاریخ ایجاد", )
    published = models.BooleanField("وضعیت انتشار", default=False)
