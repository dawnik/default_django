from django.urls import path, include
from . import views
from django.contrib.auth import views as django_default_views

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('login', django_default_views.LoginView.as_view(),     name='login'),
    path('logout', django_default_views.LogoutView.as_view(), name='logout'),
]
