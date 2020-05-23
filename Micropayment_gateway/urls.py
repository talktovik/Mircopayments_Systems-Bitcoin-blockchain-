from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path


urlpatterns = [
    url(r'admin/',admin.site.urls),
    url(r'', include('main.urls')),#include all the URLS which are specified at urls at main app! becuase we are not sure that how many urls should our app main contain in future.....
    url(r'', include('users.urls')),
    url(r'', include('blog.urls')),
    url(r'', include('mytransactions.urls')),
    url(r'', include('blockchain.urls')),
    url(r'', include('thepanel.urls')),
]
