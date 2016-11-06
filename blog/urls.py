from django.conf.urls import url

from blog import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<blog_entry_id>\d+)/$', views.view_blog_entry,
        name='blog_entry'),
]
