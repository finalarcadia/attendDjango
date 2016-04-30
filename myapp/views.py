#models
from django.contrib.auth.models import User, Group
from .models import Class, University, UserDetail, ClassRoster, Attendance, ClassRequest
#serializers
from .serializers import UserSerializer, ClassSerializer, AuthSerializer, UniversitySerializer, UserDetailSerializer, ClassRosterSerializer, AttendanceSerializer, ClassRequestSerializer
#viewsets
from rest_framework import viewsets
#classviews
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#generic classes
from rest_framework import generics
#authentication
from django.contrib.auth import authenticate
#filters
from rest_framework.filters import DjangoFilterBackend
#datees
from django.utils import timezone
import datetime

"""
Viewsets have predefined get/post/delete functionality for a queryset.
These are generic and cannot (AFIK) get input from client, so instead
use the Classviews bellow for specific querries from client
"""

#/myapp/users
#Can use this to create users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['username', 'password']

#/myapp/classes
"""
Filter example:
/myapp/classes/?universityKey=1
"""
class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['universityKey']
    
#/myapp/universities   
class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    
#/myapp/userdetails
#Can use this to create users
class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['userIdKey', 'universityKey']

#/myapp/attendance    
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['userIdKey', 'classkey', 'mark']
    
#/myapp/roster    
class ClassRosterViewSet(viewsets.ModelViewSet):
    queryset = ClassRoster.objects.all()
    serializer_class = ClassRosterSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['userIdKey', 'classIdKey']
    
#/myapp/requests    
class ClassRequestViewSet(viewsets.ModelViewSet):
    queryset = ClassRequest.objects.all()
    serializer_class = ClassRequestSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['userIdKey', 'classIdKey']
    
    
"""
Classviews can take input, as variables, from the url through correct routing
Use this data to perform whatever querries you want on the server
GET methods return data to client, while POST methods write data to server
"""

"""
/myapp/auth/usr/pw
Given usr and pw, authenticate and return user object.
ie: /myapp/auth/andresgalban/hollywood (if user is created), otherwise 404
For reference also see: AuthSerializer in serializes.py, url that corresponds to
"""
class AuthView(APIView):
    #my own method that authenticates based on input from URL
    def get_object(self, usr, pw):
        user = authenticate(username=usr, password=pw)
        if user is not None:
            # the password verified for the user
            return User.objects.get(username=usr)
        else:
            # the authentication system was unable to verify the username and password
            raise Http404

    def get(self, request, usr, pw, format=None):
        user = self.get_object(usr, pw)
        serializer = AuthSerializer(user)
        return Response(serializer.data)
        
"""
/myapp/usersfromuniversity/pk
list of all students from a given university pk
"""
class UserUniversityView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        university = self.kwargs['pk']
        users = set()
        for u in UserDetail.objects.filter(universityKey_id=university).select_related('userIdKey'):
            users.add(u.userIdKey)
        return list(users)
        
"""
/myapp/usersfromclass/pk
list of all students from a given class pk
"""
class UserClassListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        classx = self.kwargs['pk']
        users = set()
        for u in ClassRoster.objects.filter(classIdKey_id=classx).select_related('userIdKey'):
            users.add(u.userIdKey)
        return list(users)
        
"""
/myapp/classesfromuser/pk
list of all classes a given user is enrolled in
"""
class ClassUserListView(generics.ListAPIView):
    serializer_class = ClassSerializer

    def get_queryset(self):
        usrx = self.kwargs['pk']
        classes = set()
        for c in ClassRoster.objects.filter(userIdKey_id=usrx).select_related('classIdKey'):
            classes.add(c.classIdKey)
        return list(classes)
        
"""
/myapp/requestsfromuser/pk
"""
class RequestUserListView(generics.ListAPIView):
    serializer_class = ClassRequestSerializer

    def get_queryset(self):
        usrx = self.kwargs['pk']
        classes = set()
        requests = set()
        for c in ClassRoster.objects.filter(userIdKey_id=usrx).select_related('classIdKey'):
            classes.add(c.classIdKey)
        for clx in list(classes):
            for r in clx.classrequest_set.all():
                requests.add(r)
        return list(requests)
        
"""
/myapp/requestsfromuniversity/pk
"""
class RequestUniversityListView(generics.ListAPIView):
    serializer_class = ClassRequestSerializer

    def get_queryset(self):
        unipk = self.kwargs['pk']
        classes = set()
        requests = set()
        for c in University.objects.get(universityPK=unipk).class_set.all():
            classes.add(c)
        for clx in list(classes):
            for r in clx.classrequest_set.all():
                requests.add(r)
        return list(requests)
        
"""
/myapp/roster/pk/class
Mark attendance for given user pk and class
"""
class RecordView(APIView):

    def getTime(var):
        return datetime.time(var.hour, var.minute, var.second)

    def post(self, request, pk, classpk, format=None):
        c = Class.objects.get(classPK=classpk)
        
        now = datetime.datetime.now()
        start = c.start
        late = start + datetime.timedelta(minutes=c.lateThreshold)
        absent = start + datetime.timedelta(minutes=c.absentThreshold)
        now = datetime.time(now.hour, now.minute, now.second)
        start = datetime.time(start.hour, start.minute, start.second)
        late = datetime.time(late.hour, late.minute, late.second)
        absent = datetime.time(absent.hour, absent.minute, absent.second)
        
        if (now < start):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif (now <= late):
            mrk = 'present'
        elif (now <= absent):
            mrk = 'late'
        else:
            mrk = 'absent'
        
        record = Attendance(mark=mrk, classkey=Class.objects.get(classPK=classpk), userIdKey=User.objects.get(id=pk))
        record.save()
        serializer = AttendanceSerializer(record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)