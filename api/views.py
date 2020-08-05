from django.shortcuts import render
from rest_framework import viewsets
from .models import User,ActivityPeriod
from .serializers import UserSerializer,ActivityPeriodSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('real_name')
    serializer_class = UserSerializer
    #lookup_field = 'pk'

class ActivityPeriodViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all().order_by('id')
    serializer_class = ActivityPeriodSerializer

