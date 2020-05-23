from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blockchain import views
from blockchain.views import *

urlpatterns = [

    url('^get_chain$', views.get_chain, name="get_chain"),
    url('^mine_block$', views.mine_block, name="mine_block"),
    url('^is_valid$', views.is_valid, name="is_valid"),
    url('^testing', views.testing, name="testing"),
    #url('^thechain', views., name="testing"),


]
