from django.conf.urls import  url

from blog import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<blog_entry_id>\d+)/$', views.view_blog_entry,
        name='blog_entry'),
    # url(r'^(?P<question_id>\d+/results/)$', views.results, name='results'),
    # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote')
]
