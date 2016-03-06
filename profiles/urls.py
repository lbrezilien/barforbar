from django.conf.urls import include, url, patterns
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login$', views.login, name='profiles_login'),
    url(r'^update_account$', views.update_account, name='update_account'),
    url(r'^update_about$', views.update_about, name='update_about'),
    url(r'^change-password/', auth_views.password_change),

]
