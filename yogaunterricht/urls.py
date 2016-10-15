from django.conf.urls import url

from yogaunterricht import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
