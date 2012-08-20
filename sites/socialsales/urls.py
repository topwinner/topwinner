from django.conf.urls import patterns, include, url
from socialsales import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='socialsales_index'),
)
