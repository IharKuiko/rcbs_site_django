from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('category/<str:slug>/', get_category, name='category'),
    path('post/<str:slug>/', get_post, name='post'),
    # path('', views.index, name='index'),
]
