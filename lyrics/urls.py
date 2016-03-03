from django.conf.urls import include, url, patterns
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='lyrics_index'),
    url(r'^new$', views.new, name='lyrics_new'),
    url(r'^create$', views.create, name='lyrics_create'),



]
