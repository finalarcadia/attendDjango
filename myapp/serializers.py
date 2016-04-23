from django.contrib.auth.models import User, Group
from rest_framework import serializers
#import our models
from .models import Class, UniversityDim


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        
class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UniversityDim
        fields = ('universityName', 'universityCode')
        
class ClassSerializer(serializers.HyperlinkedModelSerializer):
    universityKey = UniversitySerializer()
    
    class Meta:
        model = Class
        fields = ('classId', 'name', 'startTime', 'endTime',
        'startDate', 'endDate', 'universityKey')