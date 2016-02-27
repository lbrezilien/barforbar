from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login', views.home, name='login'),
    url(r'^signup', views.home, name='signup'),
    url(r'^logout', views.home, name='logout'),

]
