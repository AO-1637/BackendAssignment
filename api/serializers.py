from rest_framework import serializers
from .models import User, ActivityPeriod

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['id','start_time','end_time']

class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)

    '''
    activity_periods - additional field not included in the model
    and exclusive to the serializer. This is a list of ActivityPeriod
    model objects that belong to the same user.
    '''

    class Meta:
        model = User
        fields = ['user_id','real_name','tz','activity_periods']

    '''
    Since this is a writable nested serializer,
    its not supported implicitly by drf.
    We are required to write custom create and update methods
    '''

    def create(self, validated_data):
        activity_periods_data = validated_data.pop('activity_periods')
        user = User.objects.create(**validated_data)
        for activity_period_data in activity_periods_data:
            ActivityPeriod.objects.create(user=user, **activity_period_data)
        return user








