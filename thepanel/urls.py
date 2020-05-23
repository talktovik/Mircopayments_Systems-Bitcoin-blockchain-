from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^vikpanel/$',views.panel, name='panel'),
    url(r'^viklist/$',views.panellist, name='panellist'),
    url(r'^vikblock/$',views.vikblock, name='vikblock'),


]