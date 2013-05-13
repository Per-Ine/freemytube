from django.conf.urls import patterns, include, url
from core.api import MainFrameResource, UserResource, LocationResource, VideoResource, MeasurementResource

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
    url(r'^admin/', include(admin.site.urls)),
)
