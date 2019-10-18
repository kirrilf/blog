from django.db import models

from django.shortcuts import reverse

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    datePub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_absolute_url(self):
        return reverse("postDetailUrl", kwargs={"slug": self.slug})
    

    def __str__(self):
        return '{}'.format(self.title)

     
class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)


    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse("tagDetailUrl", kwargs={"slug": self.slug})