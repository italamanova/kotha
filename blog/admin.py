from django.contrib import admin
from .models import Post, Category, Blogger, Comment

admin.site.register(Blogger)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)