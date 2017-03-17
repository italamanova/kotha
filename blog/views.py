from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django_tables2 import SingleTableView

from blog.forms import PostForm
from blog.models import Post, Blogger, Category



class PostListView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.all()
        return posts


class PostListByCategoryView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        #category_id = self.request.GET.get('category_id')
        posts = super(PostListByCategoryView, self).get_queryset()
        return posts.filter(category=Category.objects.get(pk = self.kwargs['category_id']))


class PostDetailView(DetailView):
    model = Post
    query_pk_and_slug = True
    pk_url_kwarg = 'post_id'
    template_name = 'blog/post_detail.html'

    def get(self, request, **kwargs):
        self.object = self.get_object()
        self.object.view()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    query_pk_and_slug = True
    pk_url_kwarg = 'post_id'
    template_name = 'blog/post_create_form.html'

    def get_success_url(self):
        return reverse('blog:list')


def about(request):
    user = Blogger.objects.filter(name='ira')[0]
    context = {'user': user}
    return render(request, 'blog/about.html', context)
