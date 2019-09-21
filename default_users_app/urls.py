from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as django_default_views

urlpatterns = [
    url('termin', views.termin, name='termin'),
    url('register', views.register_view, name='register'),
    url('profile', views.profile_user_view, name='profile'),
    url('login', django_default_views.LoginView.as_view(template_name='default_users_app/login.html'),     name='login'),
    url('logout', django_default_views.LogoutView.as_view(template_name='default_users_app/logout.html'), name='logout'),
]
