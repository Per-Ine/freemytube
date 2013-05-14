from django.conf.urls import patterns, include, url
from rest_framework import routers
from core import views
from core.views import ListMainFrames, ListLocation

# Uncomment the next two lines to enable the admiUserResource, LocationResource, VideoResource, MeasurementResourcen:
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('core.views',
    # Examples:
    # url(r'^$', 'freemytube.views.home', name='home'),
    # url(r'^freemytube/', include('freemytube.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^mainFrame/$', ListMainFrames.as_view()),
    url(r'^location/$', ListLocation.as_view()),
)