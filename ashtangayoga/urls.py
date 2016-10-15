from django.conf.urls import url

from ashtangayoga import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
