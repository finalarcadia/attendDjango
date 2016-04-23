#models
from django.contrib.auth.models import User, Group
from .models import Class
#serializers
from .serializers import UserSerializer, GroupSerializer, ClassSerializer, AuthSerializer
#viewsets
from rest_framework import viewsets
#classviews
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#authentication
from django.contrib.auth import authenticate

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

#/myapp/groups
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

#/myapp/classes    
class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    
    
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