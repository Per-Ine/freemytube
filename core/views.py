from django.contrib.auth.models import User

from core.models import MainFrame, Measurement, Video
from core.serializers import MeasurementSerializer, VideoSerializer

from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response

import django_filters


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


class MeasurementFilter(django_filters.FilterSet):
    min_date = django_filters.DateTimeFilter(lookup_type='gte')
    max_date = django_filters.DateTimeFilter(lookup_type='lte')

    class Meta:
        model = Measurement
        fields = ['user', 'video', 'start_time', 'end_time', 'minimum', 'maximum', 'average']


class UserMeasurementViewSet(generics.ListAPIView):
    model = Measurement
    serializer_class = MeasurementSerializer
    filter_class = MeasurementFilter

    def get_queryset(self):
        username = self.kwargs['username']
        return Measurement.objects.filter(user__username=username)


#________________________________________________________________________#
class UserMeasurementAdd(generics.CreateAPIView):
    model = Measurement
    serializer_class = MeasurementSerializer

    def post(self):
        serializer = MeasurementSerializer(data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


