from django.conf.urls import patterns, include, url, static

from django.conf import settings
from stuntperformers.views import test
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'startup.views.home', name='home'),
    url(r'^newsletter', 'startup.views.newsletter', name='newsletter'),
    url(r'^news', 'startup.views.news', name='news'),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^example/', include('example.urls', namespace="example")),
    #stunt performers
	url(r'^stuntperformers/', include('stuntperformers.urls', namespace="stuntperformers")),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),    
    



)

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
