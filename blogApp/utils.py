from django.shortcuts import render, get_object_or_404, redirect

from .models import *


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, 
        context={self.model.__name__.lower(): obj})


class ObjectListMixin:
    model = None
    template = None
    
    def get(self, request):
        obj = self.model.objects.all()
        return render(request, self.template,
        context={self.model.__name__.lower()+'s':obj})


class ObjectCreateMixin:

    formModel = None
    template = None

    def get(self, request):
        form = self.formModel()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        boundForm = self.formModel(request.POST)
        if boundForm.is_valid():
            newObj = boundForm.save()
            return redirect(newObj)
        return render(request, self.template, context={'form': boundForm})
