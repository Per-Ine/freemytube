from rest_framework import serializers

from core.models import Measurement, Video


class UserMeasurementSerializer(serializers.Serializer):
	start_time = serializers.DateTimeField()
	end_time = serializers.DateTimeField()
