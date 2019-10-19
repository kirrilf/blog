from django.urls import path

from .views import *

urlpatterns = [
    path('', PostsList.as_view(), name='postListUrl'),
    path('post/create/', PostCreate.as_view(), name='postCreateUrl'),
    path('post/<str:slug>/', PostDetail.as_view(), name='postDetailUrl'),
    path('tags/', TagsList.as_view(), name='tagsListUrl'),
    path('tag/create/', TagCreate.as_view(), name='tagCreateUrl'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tagDetailUrl'),

]