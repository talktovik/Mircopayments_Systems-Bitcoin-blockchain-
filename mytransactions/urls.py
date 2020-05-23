from django.conf.urls import url
from . import views # importing everything from local View

urlpatterns = [
    url(r'^start/$',views.starttransaction, name='starttransaction'),
    url(r'^confirm/$',views.confirmation, name='confirmation'),
]