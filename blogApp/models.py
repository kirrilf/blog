from django.db import models

from django.shortcuts import reverse

from django.utils.text import slugify

from time import time

def genSlug(s):
    newSlug = slugify(s, allow_unicode=True)
    return newSlug + '-' + str(int(time()))



class Post(models.Model): 
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, blank = True)
    body = models.TextField(blank=True, db_index=True)
    datePub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_absolute_url(self):
        return reverse("postDetailUrl", kwargs={"slug": self.slug})
    
    def getUpdateUrl(self):
        return reverse('postUpdateUrl', kwargs={"slug": self.slug})

    def getDeleteUrl(self):
        return reverse('postDeleteUrl', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = genSlug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-datePub']
     
class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def getUpdateUrl(self):
        return reverse('tagUpdateUrl', kwargs={"slug": self.slug})
        
    def getDeleteUrl(self):
        return reverse('tagDeleteUrl', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tagDetailUrl", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']