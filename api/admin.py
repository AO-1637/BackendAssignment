from django.contrib import admin
from .models import User
from .models import ActivityPeriod

'''
The models defined in the api app
are registered with the admin panel
'''

admin.site.register(User)
admin.site.register(ActivityPeriod)
