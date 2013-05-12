from django.conf.urls import patterns, include, url
from tastypie.api import Api
from core.api import MainFrameResource, UserResource, LocationResource, VideoResource, MeasurementResource

# Uncomment the next two lines to enable the admiUserResource, LocationResource, VideoResource, MeasurementResourcen:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='freemytube')
v1_api.register(MainFrameResource())
v1_api.register(UserResource())
v1_api.register(LocationResource())
v1_api.register(VideoResource())
v1_api.register(MeasurementResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freemytube.views.home', name='home'),
    # url(r'^freemytube/', include('freemytube.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
