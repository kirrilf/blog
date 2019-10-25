from django.shortcuts import render, get_object_or_404, redirect

from .models import *

from django.core.paginator import Paginator

from django.db.models import Q

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'adminObject':obj, 'detail':True })


class ObjectListMixin:
    model = None
    template = None
    
    def get(self, request):
        searchQuery = request.GET.get('search', '')

        if searchQuery:
            obj = self.model.objects.filter(Q(title__icontains=searchQuery) | Q(body__icontains=searchQuery))
        else:
            obj = self.model.objects.all()
        



        
        paginator = Paginator(obj, 5)
        pageNumber = request.GET.get('page', 1)

       

        page = paginator.get_page(pageNumber)

        isPaginator = page.has_other_pages()

        if page.has_previous():
            prevUrl = '?page={}'.format(page.previous_page_number())
        else:
            prevUrl = ''

        if page.has_next():
            nextUrl = '?page={}'.format(page.next_page_number())
        else:
            nextUrl = ''

        context = {
            self.model.__name__.lower()+'s':page, 
            'isPaginator': isPaginator, 
            'nextUrl':nextUrl, 
            'prevUrl': prevUrl
        }

        return render(request, self.template, context=context)


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

class ObjectUpdateMixin:
    formModel = None
    form = None
    template = None
    def get(self, request, slug):
        obj = self.form.objects.get(slug__iexact=slug)
        boundForm = self.formModel(instance=obj)
        return render(request, self.template, context={'form':boundForm, 'obj':obj})

    def post(self, request, slug):
        obj = self.form.objects.get(slug__iexact=slug)
        boundForm = self.formModel(request.POST, instance=obj)

        if boundForm.is_valid():
            updateObj = boundForm.save()
            return redirect(updateObj)

        return render(request, self.template, context={'form':boundForm, 'obj':obj})

class ObjectDeleteMixin:
    form = None
    template = None
    redirectUrl = None

    def get(self, request, slug):
        obj = self.form.objects.get(slug__iexact=slug)
        return render(request, self.template, context={'obj':obj})

    def post(self, request, slug):
        obj = self.form.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirectUrl))
        