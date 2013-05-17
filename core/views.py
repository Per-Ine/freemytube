from django.contrib.auth.models import User, Group
from django.http import HttpResponse

from core.models import MainFrame, Measurement, Video
from core.serializers import MeasurementSerializer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import permissions


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


class VideoCreateView(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = Video

    def post(self, request, format=None):
        data=request.DATA
        print data
        serializer = VideoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserStats(APIView):

    model = Measurement

    def get(self, request, user_id=None, *args, **kwargs) :

        measurement = Measurement.objects.filter(user__id=user_id)
        serializer = MeasurementSerializer(measurement, many=True)

        return Response(serializer.data)
