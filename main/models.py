'''
the models.py is the file where we define the structure of our database
'''


from __future__ import unicode_literals #all now it sustain all langauges.
from django.db import models


# Create your models here.
class Main(models.Model):# class name is capital. remember that!
    Name = models.CharField(max_length=30)
    vikas = models.TextField(default="-")
    tag = models.TextField(max_length=200,default="-")


    def __str__(self):
        return self.Name +"|" + str(self.pk)



class MainSub(models.Model): # I am creating this
    update = models.TextField()
    name = models.TextField()
    proof_of_work = models.TextField()
    documentation = models.TextField()
    charges_rules = models.TextField()

    def __str__(self):
        return self.update + str(self.pk) #this will show the name for eg, on database and if we remove this function then we will seee something like "Main object (1)" that alse can be know as pika number
