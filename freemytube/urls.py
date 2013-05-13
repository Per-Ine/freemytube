from django.conf.urls import patterns, include, url
from tastypie.api import Api
from core.api import MainFrameResource, UserResource, LocationResource, VideoResource, MeasurementResource

# Uncomment the next two lines to enable the admiUserResource, LocationResource, VideoResource, MeasurementResourcen:
from django.contrib import admin
admin.autodiscover()

freemytube_api = Api(api_name='freemytube')
freemytube_api.register(MainFrameResource())
freemytube_api.register(UserResource())
freemytube_api.register(LocationResource())
freemytube_api.register(VideoResource())
freemytube_api.register(MeasurementResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freemytube.views.home', name='home'),
    # url(r'^freemytube/', include('freemytube.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(freemytube_api.urls)),
)
