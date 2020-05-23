from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^sign-up/$',views.my_register, name='my_register'),
    url(r'^log-in/$',views.mylogin, name='mylogin'),
    url(r'^profile/$',views.profile,name= 'profile'),
    url(r'^logout/$',views.mylogout,name= 'mylogout'),
    url(r'^profile/userlist/$',views.userlist,name= 'userlist'),
    url(r'^profile/myqrcode/$',views.theqrcode,name= 'theqrcode'),


]