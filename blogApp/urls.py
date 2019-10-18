from django.urls import path

from .views import *

urlpatterns = [
    path('', postsList, name='postListUrl'),
    path('post/<str:slug>/', postDetail, name='postDetailUrl'),
    path('tags/', tagsList, name='tagsListUrl'),
    path('tag/<str:slug>', tagDetail, name='tagDetailUrl'),
]