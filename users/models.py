from __future__ import unicode_literals
from django.db import models
# Create your models here.

class UsersData(models.Model):# class name is capital. remember that!
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    email= models.CharField(max_length=50)
    vikcoin = models.IntegerField(default=100)

    def __str__(self):
        return self.username + " | " + str(self.pk)