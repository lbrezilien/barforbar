from django.conf.urls import include, url, patterns
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^change-password/', auth_views.password_change),

]
