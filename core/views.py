from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import MainFrame
from core.serializers import MainFrameSerializer

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


#class JSONResponse(HttpResponse):
#    """
#    An HttpResponse that renders it's content into JSON.
#    """
#    def __init__(self, data, **kwargs):
#        content = JSONRenderer().render(data)
#        kwargs['content_type'] = 'application/json'
#        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET', 'POST'])
def frame_list(request):
    """
    List all frame, or create a new frame.
    """
    if request.method == 'GET':
        frame = MainFrame.objects.all()
        serializer = MainFrameSerializer(frame, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        serializer = MainFrameSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def frame_details(request, pk):
    """
    Retrieve, update or delete a code main frame.
    """
    try:
        frame = MainFrame.objects.get(pk=pk)
    except MainFrame.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MainFRameSerializer(frame)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MainFrameSerializer(frame, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        frame.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)