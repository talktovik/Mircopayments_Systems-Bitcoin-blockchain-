from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^blog/$',views.blog, name='blog'),
    url(r'^blog/add/$',views.add, name='add'), #okay there was a error because the name add was incorrect, thats very important during the taking data
    url(r'^function/$',views.function, name='function'),
]