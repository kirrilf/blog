from django.urls import path

from .views import *

urlpatterns = [
    path('', PostsList.as_view(), name='postListUrl'),
    path('post/create/', PostCreate.as_view(), name='postCreateUrl'),
    path('post/<str:slug>/', PostDetail.as_view(), name='postDetailUrl'),
    path('post/<str:slug>/update', PostUpdate.as_view(), name='postUpdateUrl'),
    path('post/<str:slug>/delete', PostDelete.as_view(), name='postDeleteUrl'),
    path('tags/', TagsList.as_view(), name='tagsListUrl'),
    path('tag/create/', TagCreate.as_view(), name='tagCreateUrl'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tagDetailUrl'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tagUpdateUrl'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tagDeleteUrl'),
]