from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
 
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control'})
        }



    def clean_slug(self):
        newSlug = self.cleaned_data['slug'].lower()

        if newSlug == 'create':
            raise ValidationError('Slug may not be "create"')
        if Tag.objects.filter(slug__iexact=newSlug).count():
            raise ValidationError('Slug must be unique. We have "{}" already slug'.format(newSlug))
        return newSlug



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}), 
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class':'form-control'})
        }

    def  clean_slug(self):
        newSlug = self.cleaned_data['slug'].lower()

        if newSlug == 'create':
            raise ValidationError('Slug may not be "create"')
        return newSlug