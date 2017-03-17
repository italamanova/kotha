from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone


class Blogger(AbstractBaseUser):
    name = models.CharField(default='ira', max_length=200)
    photo = models.ImageField(upload_to='user_photos',null=True, blank=True)
    about_short = models.TextField(null=True, blank=True)
    about_long = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'name'


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    category = models.ForeignKey('Category')
    image = models.ImageField(null=True, blank=True)
    views = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def view(self):
        self.views += 1;
        self.save()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
