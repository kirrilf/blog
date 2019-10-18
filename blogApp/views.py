from django.shortcuts import render

from django.http import HttpResponse

from .models import Post, Tag

def postsList(request):
    posts = Post.objects.all()
    return render(request, 'blogApp/index.html', context={'posts':posts})
 
def postDetail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blogApp/postDetail.html', context={'post':post})
      
def tagsList(request):
    tags = Tag.objects.all()
    return render(request, 'blogApp/tagsList.html', context={'tags': tags})

def tagDetail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blogApp/tagDetail.html', context={'tag':tag})