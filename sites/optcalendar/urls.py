from django.conf.urls.defaults import patterns, include, url
from optcalendar import views

urlpatterns = patterns('',
<<<<<<< HEAD
    url(r'^$', views.index, name='optcalendar_index'),
=======
    url(r'^$', views.index, name='optcalendar'),
>>>>>>> origin/master
)
