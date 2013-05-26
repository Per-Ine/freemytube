from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from core import views
from core.views import UserMeasurementViewSet, UserMeasurementAdd


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'mainframes', views.MainFrameViewSet)
router.register(r'videos', views.VideoViewSet)
router.register(r'measurements', views.MeasurementViewSet)


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^token-auth/', 'obtain_auth_token'),

    url(r'^measurements/(?P<username>.+)/$', UserMeasurementViewSet.as_view()),
    url(r'^measurements/add/$', UserMeasurementAdd.as_view()),

    url(r'^', include(router.urls)),
)
