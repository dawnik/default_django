from django.urls import path
from . import views
app_name = 'training'
urlpatterns = [
    path('tindex/', views.t_index, name='t_index'),
    path('t/<int:training_id>/', views.t_detail, name='t_detail'),
]