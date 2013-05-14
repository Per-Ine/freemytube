from django.contrib.auth.models import User, Group
from django.http import HttpResponse

from core.models import MainFrame
from core.serializers import UserSerializer, GroupSerializer
from core.serializers import MainFrameSerializer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#from rest_framework import authentication, permissions


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

        frame = MainFrame.objects.all()
        serializer = MainFrameSerializer(frame, many=True)

        return JSONResponse(serializer.data)