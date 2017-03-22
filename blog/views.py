from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django_tables2 import SingleTableView

from blog.forms import PostForm, CommentForm
from blog.models import Post, Blogger, Category, Comment


class PostListView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.all().order_by('-published_date')
        return posts


class PostListByCategoryView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # category_id = self.request.GET.get('category_id')
        posts = super(PostListByCategoryView, self).get_queryset()
        return posts.filter(
            category=Category.objects.get(pk=self.kwargs['category_id']))


# class PostDetailView(DetailView):
#     model = Post
#     query_pk_and_slug = True
#     pk_url_kwarg = 'post_id'
#     template_name = 'blog/post_detail.html'
#
#     def get(self, request, **kwargs):
#         self.object = self.get_object()
#         self.object.view()
#         context = self.get_context_data(object=self.object)
#         return self.render_to_response(context)
#
#         # def get_context_data(self, **kwargs):
#         #     context = super(PostDisplay, self).get_context_data(**kwargs)
#         #     context['form'] = CommentForm()
#         #     return context
#
#
# class CommentView(SingleObjectMixin, FormView):
#     template_name = 'books/post_detail.html'
#     form_class = CommentForm
#     slug_field = 'post_id'
#     model = Comment
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super(CommentView, self).post(request, *args, **kwargs)
#
#     def get_success_url(self):
#         return reverse('post_detail', kwargs={'pk': self.object.pk})


def post_detail_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(reverse('blog:detail', kwargs={'post_id': post.id}))
    context = {'post': post, 'comments': post.comment_set.all()}
    context['comment_form'] = CommentForm()
    return render(request, 'blog/post_detail.html', context)


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
