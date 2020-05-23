'''
this file will help us to register the app
'''

from django.contrib import admin
from .models import Main
from .models import MainSub #registering or models here

# Register your models here.

admin.site.register(Main)#registering my app and the CLASS MAIN thats very important to understand.
admin.site.register(MainSub) #its actually defining the models value here like mainsub class here. and then only we can see it our in our admin
