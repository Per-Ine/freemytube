from tastypie.resources import ModelResource
from django.contrib.auth.models import User
#from tastypie.authentication import ApiKeyAuthentication
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields

from core.models import Location, MainFrame, Video, Measurement

#from django.db import models
#from tastypie.models import create_api_key

#models.signals.post_save.connect(create_api_key, sender=User)

class MainFrameResource(ModelResource):
    class Meta:
        queryset = MainFrame.objects.all()
        resource_name = 'mainFrame'
        authorization = DjangoAuthorization()


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()


class LocationResource(ModelResource):

    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'


class VideoResource(ModelResource):
    class Meta:
        queryset = Video.objects.all()
        resource_name = 'video'

class MeasurementResource(ModelResource):

    location = fields.ForeignKey(LocationResource, 'location')

    class Meta:
        queryset = Measurement.objects.all()
        resource_name = 'measurement'
        fields = ['start_time', 'end_time', 'minimum', 'maximum', 'average', 'file_size']