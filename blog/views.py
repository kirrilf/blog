from django.http import HttpResponse
from django.shortcuts import redirect

def redirectBlogApp(request):
    return redirect('postListUrl', permanent=True)
