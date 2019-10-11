from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('context2', views.render_context_in_page_method_2, name='context2'),
    path('context/', views.render_context_in_page, name='context'),
]
