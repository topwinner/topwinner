from django.conf.urls.defaults import patterns, urls, url
from helpcenter import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='helpcenter_index'),
)
