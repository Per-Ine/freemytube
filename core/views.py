from django.contrib.auth.models import User

from core.models import MainFrame, Measurement, Video
from core.serializers import MeasurementSerializer, VideoSerializer

from rest_framework import viewsets, generics
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


class UserMeasurementList(generics.ListAPIView):
    model = Measurement
    serializer_class = MeasurementSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        return Measurement.objects.filter(user__username=username)



class UserVideo(APIView):

    model = Video

    def get(self, request, video_id=None, *args, **kwargs):

        video = Video.objects.filter(id=video_id)
        serializer = VideoSerializer(video, many=True)

        return Response(serializer.data)

