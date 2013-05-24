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


class UserMeasurementViewSet(generics.ListAPIView):
    model = Measurement
    serializer_class = MeasurementSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        queryset = Measurement.objects.filter(user__username=username)
        #queryset = queryset.filter(start_time__year='2012')

        s_date = self.request.QUERY_PARAMS.get('start_time', None)
        if s_date is not None:
            queryset = queryset.filter(start_time=s_date)

        e_date = self.request.QUERY_PARAMS.get('end_time', None)
        if e_date is not None:
            queryset = queryset.filter(end_time=e_date)

        return queryset


#________________________________________________________________________#
class UserMeasurementAdd(generics.CreateAPIView):
    model = Measurement
    serializer_class = MeasurementSerializer

    def post(self, request, *args, **kwargs):
        data = request.DATA
        serializer = MeasurementSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


