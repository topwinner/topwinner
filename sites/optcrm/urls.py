from django.conf.urls import patterns, include, url
from optcrm import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='optcrm_index'),
)
