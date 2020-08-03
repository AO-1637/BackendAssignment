from rest_framework import serializers
from .models import User, ActivityPeriod

'''
HyperlinkedModelSerializers have been used to display
activity periods as links rather than as json representation
'''

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['startTime','endTime']

class UserSerializer(serializers.ModelSerializer):
    activityPeriods = ActivityPeriodSerializer(many=True)
    class Meta:
        model = User
        fields = ['userId','realName','tz','activityPeriods']
        depth = 1
        '''
        if depth is removed,
        only the ids will be displayed for activityPeriods
        '''
        def create(self, validated_data):
            activityPeriods = validated_data.pop('choices')
            user = User.objects.create(**validated_data)
            for activity in activityPeriods:
                ActivityPeriod.objects.create(**activity, User = user)
            return user







