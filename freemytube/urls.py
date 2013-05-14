from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers

from core.views import ListMainFrames

# Uncomment the next two lines to enable the admiUserResource, LocationResource, VideoResource, MeasurementResourcen:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freemytube.views.home', name='home'),
    # url(r'^freemytube/', include('freemytube.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^core/', include('core.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^mainFrame/$', 'core.views.frame_list'),
    url(r'^mainFrame2/$', ListMainFrames.as_view()),
    url(r'^mainFrame/(?P<pk>[0-9]+)/$', 'core.views.frame_details'),
)