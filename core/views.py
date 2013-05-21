from django.contrib.auth.models import User

from core.models import MainFrame, Measurement, Video
from core.serializers import MeasurementSerializer, VideoSerializer

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

#________________________________________________________________________#


class UserMeasurementViewSet(APIView):

    model = Measurement

    def get(self, request, user_name=None, *args, **kwargs):

        measurement = Measurement.objects.filter(user__username=user_name)
        serializer = MeasurementSerializer(measurement, many=True)

        return Response(serializer.data)


class UserVideo(APIView):

    model = Video

    def get(self, request, video_id=None, *args, **kwargs):

        video = Video.objects.filter(id=video_id)
        serializer = VideoSerializer(video, many=True)

        return Response(serializer.data)

