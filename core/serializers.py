from django.contrib.auth.models import User, Group
from rest_framework import serializers

from core.models import MainFrame, Video, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('user', 'minimum', 'maximum', 'average', 'start_time', 'end_time', 'file_size')
