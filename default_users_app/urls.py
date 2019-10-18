from django.conf.urls import url, include
from django.urls import path, include
from . import views
from django.contrib.auth import views as django_default_views

app_name = 'default_users_app'
urlpatterns = [
    path('termin', views.termin, name='termin'),
    path('register', views.register_view, name='register'),
    path('profile', views.profile_user_view, name='profile'),
    path('login', django_default_views.LoginView.as_view(template_name='default_users_app/login.html'), name='login'),
    path('logout', django_default_views.LogoutView.as_view(template_name='default_users_app/logout.html'), name='logout'),
]
