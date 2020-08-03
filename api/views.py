from django.shortcuts import render
from rest_framework import viewsets
from .models import User,ActivityPeriod
from .serializers import UserSerializer,ActivityPeriodSerializer

'''
Viewset classes for User and ActivityPeriod models have been defined.
Viewsets provide a single api root where get,post,put and patch requests
can be handled.
'''

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('realName')
    serializer_class = UserSerializer

class ActivityPeriodViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer
