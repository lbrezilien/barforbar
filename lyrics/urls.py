from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='lyrics_index'),
    url(r'^new$', views.new, name='lyrics_new'),
    url(r'^create$', views.create, name='lyrics_create'),
    url(r'^(?P<id>\d+)/$', views.show, name='lyrics_show'),
    url(r'^moods$', views.moods, name='moods'),




]
