from __future__ import unicode_literals
from django.db import models


class Blockchains(models.Model):
    thechain = models.CharField(max_length=10000000)
    index = models.IntegerField(default=0)
    timestamp = models.CharField(max_length=40, default='-')
    nonce = models.IntegerField(default=1)
    previoushash = models.CharField(max_length=1000000,default=0)
    sendername = models.CharField(max_length=1000000, default='-')

    def __str__(self):
        return str(self.pk)

class Thelongestchain(models.Model):
    longestchain = models.CharField(max_length=10000000)


    def __str__(self):
        return str(self.pk)