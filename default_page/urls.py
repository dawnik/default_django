# from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'default_page'
urlpatterns = [
    path('', views.index, name='index'),
    path('showall/', views.showall, name='showall'),
    path('detail/<int:subject_id>', views.detail, name='detail'),
]
