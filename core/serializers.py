from django.forms import widgets
from rest_framework import serializers
from core.models import MainFrame, Location, Video, Measurement

class MainFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainFrame
        fields = ('name', 'town', 'nra', 'dslam', 'ip_adress')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('user', 'main_frame', 'ip_adress', 'hostname', 'zipcode', 'lon', 'lat')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('video_title', 'video-url')

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('video', 'location', 'minimum', 'maximum', 'average', 'start_time', 'end_time', 'file_size')