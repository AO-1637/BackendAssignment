'''
This file holds detail as to what views will be rendered
when a particular endpoint is hit
'''

from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('user',views.UserViewSet)
router.register('activityperiod',views.ActivityPeriodViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
