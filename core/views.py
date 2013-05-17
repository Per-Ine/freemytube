from django.contrib.auth.models import User

from core.models import MainFrame, Measurement, Video
from core.serializers import MeasurementSerializer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    model = User


class MainFrameViewSet(viewsets.ModelViewSet):
    """
    """
    model = MainFrame


class VideoViewSet(viewsets.ModelViewSet):
    """
    """
    model = Video


class MeasurementViewSet(viewsets.ModelViewSet):
    """
    """
    model = Measurement


class UserStats(APIView):

    model = Measurement

    def get(self, request, user_id=None, *args, **kwargs):

        measurement = Measurement.objects.filter(user__id=user_id)
        serializer = MeasurementSerializer(measurement, many=True)

        return Response(serializer.data)
