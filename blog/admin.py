from django.contrib import admin
from .models import Post, Category, Blogger

admin.site.register(Blogger)
admin.site.register(Post)
admin.site.register(Category)