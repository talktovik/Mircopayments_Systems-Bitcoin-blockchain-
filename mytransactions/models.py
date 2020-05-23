from __future__ import unicode_literals #all now it sustain all langauges.
from django.db import models


# Create your models here.
class Transactiondata(models.Model):        # class name is capital. remember that!
    transactionid =models.IntegerField()
    sendername = models.TextField(max_length=30)
    recievername = models.TextField(max_length=30)
    coin = models.IntegerField()
    ipaddress = models.TextField(max_length=30)
    timeanddate = models.TextField(max_length=30)
    transferamount = models.IntegerField(default=0)
    def __str__(self):
        return str(self.transactionid) +" | " + 'pk = ' +  str(self.pk) + " | "+  self.sendername + " to " +  self.recievername
