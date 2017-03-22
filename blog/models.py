import re

import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone
from sorl.thumbnail.shortcuts import get_thumbnail


class Blogger(AbstractBaseUser):
    name = models.CharField(default='ira', max_length=200)
    photo = models.ImageField(upload_to='user_photos', null=True, blank=True)
    about_short = models.TextField(null=True, blank=True)
    about_long = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'name'


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    # created_date = models.DateTimeField(
    #         default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    category = models.ForeignKey('Category')
    image = models.ImageField(null=True, blank=True)
    views = models.IntegerField(default=0)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def get_short_text(self):
        return ' '.join(re.split(r'(?<=[.])\s', self.text)[:3])

    def view(self):
        self.views += 1;
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=255, verbose_name=_('Author'))
    text = models.CharField(max_length=255, verbose_name=_('Text'))
    post = models.ForeignKey(Post, verbose_name=_('Post'))
    date_created = models.DateTimeField(default=timezone.now,
                                        verbose_name=_('Date created'))

    def __str__(self):
        return self.text

    def get_pretty_date_created(self):
        return datetime.datetime.strftime(self.date_created,
                                          "%d.%m.%y %H:%M")

    # def get_cropped_photo(self, *args, **kwargs):
    #     return get_thumbnail(self.photo, '40x40', crop='center')

    class Meta:
        ordering = ['-date_created']
