from django.urls import path
from . import views


app_name = 'post'

urlpatterns = [
    path('<str:category>/', views.list, name='list'),
]