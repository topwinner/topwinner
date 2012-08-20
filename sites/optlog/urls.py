from django.conf.urls import patterns, include, url
from optlog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='optlog_index'),
)
