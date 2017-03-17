from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url

from kotha import settings
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='list'),
    url(r'^post/(?P<post_id>\d+)/$', views.PostDetailView.as_view(),
        name='detail'),
    url(r'^category/(?P<category_id>\d+)/$', views.PostListByCategoryView.as_view(),
        name='list_by_category'),
    url(r'^about/$', views.about, name='about'),
    # url(r'^contact$', views.PostDetailView.as_view(),
    #     name='contact'),

    url(r'^create/$', views.PostCreateView.as_view(),
        name='post_create'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
