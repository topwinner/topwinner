from django.conf.urls import patterns, include, url
from promo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='promo_index'),
    url(r'^limitedtimediscount/$', views.limitedtimediscount, name='limitedtimediscount'),
    url(r'^fullrewards/$', views.fullrewards, name='fullrewards'),
    url(r'^buymore/$', views.buymore, name='buymore'),
    url(r'^freeshipping/$', views.freeshipping, name='freeshipping'),
)
