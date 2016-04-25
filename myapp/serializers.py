from django.contrib.auth.models import User, Group
from .models import Class, University, UserDetail, ClassRoster
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'first_name', 'last_name')

class AuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
        
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
        
class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    #must do this for Foreign Keys
    universityKey = serializers.PrimaryKeyRelatedField(queryset=University.objects.all())
    userIdKey = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = UserDetail
        fields = ('userDetailPK','userType', 'userIdKey', 'universityKey', 'schoolId')
        
class ClassRosterSerializer(serializers.HyperlinkedModelSerializer):
    #must do this for Foreign Keys
    classIdKey = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())
    userIdKey = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = ClassRoster
        fields = ('classRosterPK','classIdKey', 'userIdKey')