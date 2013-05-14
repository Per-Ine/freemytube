from django.contrib.auth.models import User, Group
from rest_framework import serializers

from core.models import MainFrame

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MainFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainFrame
        fields = ('name', 'town', 'nra', 'dslam', 'ip_adress')