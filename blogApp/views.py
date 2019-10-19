from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import View
from django.http import HttpResponse

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectListMixin, ObjectCreateMixin
from .forms import TagForm, PostForm


class PostsList(ObjectListMixin, View):
    model = Post
    template = 'blogApp/index.html'

class TagsList(ObjectListMixin, View):
    model = Tag
    template = 'blogApp/tagsList.html'


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blogApp/postDetail.html'
 
        
class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blogApp/tagDetail.html'

class TagCreate(ObjectCreateMixin, View):
    formModel  = TagForm
    template = 'blogApp/tagCreate.html'

class PostCreate(ObjectCreateMixin, View):
    formModel  = PostForm
    template = 'blogApp/postCreate.html'


