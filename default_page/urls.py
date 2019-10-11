# from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('context/', views.render_context_in_page, name='context'),
]
