from django.forms import widgets
from rest_framework import serializers
from core.models import MainFrame

class MainFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainFrame
        fields = ('name', 'town', 'nra', 'dslam', 'ip_adress')