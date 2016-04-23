from django.contrib.auth.models import User, Group
from .models import Class, University
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class AuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = ('universityPK', 'universityName')
        
class ClassSerializer(serializers.HyperlinkedModelSerializer):
    #must do this for Foreign Keys
    universityKey = serializers.PrimaryKeyRelatedField(queryset=University.objects.all())
    
    class Meta:
        model = Class
        fields = ('classPK', 'classId', 'startTime', 'endTime',
        'startDate', 'endDate', 'universityKey')