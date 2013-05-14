from django.forms import widgets
from rest_framework import serializers
from core.models import MainFrame

class MainFrameSerializer(serializers.Serializer):
    class Meta:
        model = MainFramefields = ('name', 'town', 'nra', 'dslam', 'ip_adress')