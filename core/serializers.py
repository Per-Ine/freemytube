from rest_framework import serializers

from core.models import Measurement, Video


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('user', 'minimum', 'maximum', 'average', 'start_time',
                  'end_time', 'file_size')

class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video