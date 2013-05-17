from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from core import views
from core.views import UserStats


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'mainframes', views.MainFrameViewSet)
router.register(r'videos', views.VideoViewSet)
router.register(r'measurements', views.MeasurementViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^userStats/(?P<user_id>[0-9]+)/$', UserStats.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)
