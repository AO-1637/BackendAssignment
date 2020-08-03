
from django.db import models
from timezone_utils.fields import TimeZoneField
from timezone_utils.choices import PRETTY_ALL_TIMEZONES_CHOICES

'''
The User and the ActivityPeriod models have been defined here.
There is a many to many relationship defined between them as
A user can have multiple activity periods and
An activity period can belong to multiple users
'''

class ActivityPeriod(models.Model):
    startTime = models.DateTimeField(null = True,blank = True)
    endTime = models.DateTimeField(null = True,blank = True)

class User(models.Model):
    userId = models.CharField(max_length=100,primary_key=True)
    realName = models.CharField(max_length=100)
    tz = TimeZoneField(choices=PRETTY_ALL_TIMEZONES_CHOICES)
    activityPeriods = models.ForeignKey(ActivityPeriod, on_delete=models.CASCADE, related_name='activityPeriod')
    #activityPeriods = models.ManyToManyField(ActivityPeriod)

    @property
    def activityPeriods(self):
        return self.activityPeriod_set.all()




