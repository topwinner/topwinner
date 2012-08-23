from django.conf.urls import patterns, include, url
from opthelper import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='opthelper_index'),
    url(r'^autoshelves/$', views.autoshelves, name='autoshelves'),
    url(r'^autoshowcase/$', views.autoshowcase, name='autoshowcase'),
    url(r'^bulkediting/$', views.bulkediting, name='bulkediting'),
    url(r'^salespackage/$', views.salespackage, name='salespackage'),
    url(r'^salesrecommend/$', views.salesrecommend, name='salesrecommend'),
    url(r'^groupbuytemplates/$', views.groupbuytemplates, name='groupbuytemplates'),
    url(r'^praiserecommended/$', views.praiserecommended, name='praiserecommended'),
    url(r'^watermarks/$', views.watermarks, name='watermarks'),
)
