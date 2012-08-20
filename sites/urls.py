from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from tastypie.api import Api
#from sites.api.resources import MyModelResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
#v1_api.register(MyModelResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simple_todo_site.views.home', name='home'),
    #url(r'^simple_todo_site/', include('simple_todo_site.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url('^$', 'views.index', name='idx'),
    url(r'^logout/', 'views.logout', name='logout'),
    url(r'^newfeatures/', 'views.newfeatures', name='newfeatures'),
    url(r'^userprofile/', 'views.userprofile', name='userprofile'),
    url(r'^helpcenter/', 'views.helpcenter', name='helpcenter'),
    url(r'^aboutus/', 'views.aboutus', name='aboutus'),
    url(r'^contactus/', 'views.contactus', name='contactus'),
    url(r'^reportissue/', 'views.reportissue', name='reportissue'),
    url(r'^onlineservice/', 'views.onlineservice', name='onlineservice'),

    url(r'^promo/', include('promo.urls','promo')),
    url(r'^optcalendar/', include('optcalendar.urls','optcalendar')),
    url(r'^optanalysis/',  include('optanalysis.urls','optanalysis')),
    url(r'^optlog/',include('optlog.urls','optlog')),
    url(r'^opthelper/', include('opthelper.urls','opthelper')),
    url(r'^optcrm/', include('optcrm.urls','optcrm')),
    url(r'^socialsales/',include('socialsales.urls','socialsales')),

    url(r'^ui/', include('ui.urls','ui')),
    # url(r'^api/', include(v1_api.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
