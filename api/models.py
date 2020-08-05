
from django.db import models
from timezone_utils.fields import TimeZoneField
from timezone_utils.choices import PRETTY_ALL_TIMEZONES_CHOICES

'''
The User and the ActivityPeriod models have been defined here.
There is a One-To-Many realtionship
defined between User and ActivityPeriod
as one User might have multiple ActivityPeriods associated to it.
'''

class User(models.Model):
    user_id = models.CharField(max_length=100,primary_key=True)
    real_name = models.CharField(max_length=100)
    tz = TimeZoneField(choices=PRETTY_ALL_TIMEZONES_CHOICES)

    def __str__(self):
        return self.user_id

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='activity_periods')
    '''
    One-To-Many realtionship with User with
    a reverse reference activity_periods
    '''
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return '%d: %s' % (self.id, self.user)





