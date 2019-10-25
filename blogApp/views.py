from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import View
from django.http import HttpResponse
 
from django.urls import reverse

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectListMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin



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


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    formModel  = TagForm
    template = 'blogApp/tagCreate.html'
    raise_exception = True


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    formModel  = PostForm
    template = 'blogApp/postCreate.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    formModel  = TagForm
    form = Tag
    template = 'blogApp/tagUpdate.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    formModel = PostForm
    form = Post
    template = 'blogApp/postUpdate.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    form = Tag
    template = 'blogApp/tagDelete.html'
    redirectUrl = 'tagsListUrl'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    form = Post
    template = 'blogApp/postDelete.html'
    redirectUrl = 'postListUrl'
    raise_exception = True
   