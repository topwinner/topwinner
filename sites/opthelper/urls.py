from django.conf.urls import patterns, include, url
from opthelper import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='opthelper_index'),
)
