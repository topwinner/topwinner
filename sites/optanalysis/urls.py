from django.conf.urls import patterns, include, url
from optanalysis import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='optanalysis_index'),
)
