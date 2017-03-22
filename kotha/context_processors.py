import datetime
from django.utils import timezone
from django.db.models import Count, Max, Min
from blog.models import Category, Blogger, Post


def get_owner(request):
    owner = Blogger.objects.filter(name='ira')
    return {'owner': owner[0]}


def category_list(request):
    categories = Category.objects.select_related().annotate(
        num_posts=Count('post'))
    return {'category_list': categories}


def get_popular_posts(request):
    popular_posts = Post.objects.all().order_by('-views')
    return {'popular_posts': popular_posts[:3]}


def get_recent_posts(request):
    recent_posts = Post.objects.filter(published_date__lte=timezone.now(),
                                       published_date__gt=timezone.now() - datetime.timedelta(
                                   days=7)).order_by('-published_date')
    return {'recent_posts': recent_posts[:3]}
