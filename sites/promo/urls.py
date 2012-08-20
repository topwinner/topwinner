from django.conf.urls import patterns, include, url
from promo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='promo_index'),
)
