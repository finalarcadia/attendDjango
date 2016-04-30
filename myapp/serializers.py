from django.contrib.auth.models import User, Group
from .models import Class, University, UserDetail, ClassRoster, Attendance, ClassRequest
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
        fields = ('classPK', 'classId', 'update', 'start', 'lateThreshold', 'absentThreshold',
        'codeExpiration', 'locationFlag', 'latitude', 'longitude', 'codeFlag', 'code', 'universityKey')
        
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
        
class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    #must do this for Foreign Keys
    classkey = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())
    userIdKey = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = Attendance
        fields = ('attendancePK','time', 'mark', 'classkey', 'userIdKey')
        
class ClassRequestSerializer(serializers.HyperlinkedModelSerializer):
    #must do this for Foreign Keys
    classIdKey = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())
    userIdKey = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = ClassRequest
        fields = ('classRequestPK','requestType', 'classIdKey', 'userIdKey')
