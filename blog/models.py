from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Post(models.Model):# class name is capital. remember that!
    title = models.CharField(max_length=30)
    tag= models.CharField(max_length=30)
    post = models.TextField()
    thetime = models.CharField(max_length=12 ,default ="Pre-historic")
    writer = models.CharField(max_length=40, default="")

    def __str__(self):
        return self.title +"|" + str(self.pk)