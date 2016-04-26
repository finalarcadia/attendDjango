#models
from django.contrib.auth.models import User, Group
from .models import Class, University, UserDetail, ClassRoster
#serializers
from .serializers import UserSerializer, ClassSerializer, AuthSerializer, UniversitySerializer, UserDetailSerializer, ClassRosterSerializer
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
    
#/myapp/roster    
class ClassRosterViewSet(viewsets.ModelViewSet):
    queryset = ClassRoster.objects.all()
    serializer_class = ClassRosterSerializer
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
        clax = self.kwargs['pk']
        users = set()
        for u in ClassRoster.objects.filter(classIdKey_id=clax).select_related('userIdKey'):
            users.add(u.userIdKey)
        return list(users)