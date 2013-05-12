from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields

from core.models import Location, MainFrame, Video, Measurement

class MainFrameResource(ModelResource):
    class Meta:
        queryset = MainFrame.objects.all()
        resource_name = 'mainFrame'

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']


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