'''
This is a django custom command for
adding dummy data to the model database.

It is invoked using:
python manage.py populate_db
'''

from api.serializers import UserSerializer
from django.core.management.base import BaseCommand
import json

class Command(BaseCommand):
    help = 'Populate database with dummy data'

    def handle(self, *args, **kwargs):
        user_string = '''
            {
            "user_id": "W07QCRPA4",
            "real_name": "Glinda Southgood",
            "tz": "Asia/Kolkata",
            "activity_periods": [{
                    "start_time": "2020-10-25 14:30:59",
                    "end_time": "2020-10-25 14:30:59"
                },
                {
                    "start_time": "2020-10-26 14:30:59",
                    "end_time": "2006-10-26 14:30:59"
                },
                {
                    "start_time": "2020-10-27 14:30:59",
                    "end_time": "2006-10-27 14:30:59"
                }
            ]
        }
        '''
        data = json.loads(user_string)
        serializer = UserSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            print('database populated !')

        else:
            print(serializer.errors)

