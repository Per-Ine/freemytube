from django.contrib.auth.models import User, Group
from rest_framework import serializers

from core.models import MainFrame, Location, Video, Measurement

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MainFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainFrame
        fields = ('name', 'town', 'nra', 'dslam', 'ip_adress')

class LocationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Location
        fields = ('ip_address', 'hostname', 'zipcode', 'lon', 'lat', 'user')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('video_title', 'video_url')

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('user', 'minimum', 'maximum', 'average', 'start_time', 'end_time', 'file_size')