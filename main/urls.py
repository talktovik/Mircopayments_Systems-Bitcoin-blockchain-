from django.conf.urls import url
from . import views # importing everything from local View

urlpatterns = [
    url(r'^$',views.home, name='home'), #we have a home at views which is working there in constant way
    url(r'^about/$',views.about, name='about'), #about page thing this is the second job
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^working/$',views.work, name='work')

]
