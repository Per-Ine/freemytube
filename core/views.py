from django.contrib.auth.models import User, Group
from django.http import HttpResponse

from core.models import MainFrame, Location, Measurement, Video
from core.serializers import UserSerializer, GroupSerializer, VideoSerializer
from core.serializers import MainFrameSerializer, LocationSerializer, MeasurementSerializer
from core.permissions import IsOwnerOrReadOnly

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
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class JSONResponse(HttpResponse):
   """
   An HttpResponse that renders it's content into JSON.
   """
   def __init__(self, data, **kwargs):
       content = JSONRenderer().render(data)
       kwargs['content_type'] = 'application/json'
       super(JSONResponse, self).__init__(content, **kwargs)


class ListMainFrames(APIView):

    model = MainFrame

    def get(self, request, format=None):
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        frame = MainFrame.objects.all()
        serializer = MainFrameSerializer(frame, many=True)

        return Response(serializer.data)


class ListLocation(APIView):

    model = Location


    def get(self, request, user_id=None, format=None):
        location = Location.objects.filter(user__id=user_id)
        serializer = LocationSerializer(location, many=True)

        return Response(serializer.data)

    def post(self, request, user_id=None, format=None):
        data=request.DATA
        print data
        serializer = LocationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
