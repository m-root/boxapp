from rest_framework import serializers

from .models import *

class ActivityScheduleAndCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityScheduleAndCalendar
        fields ='__all__'

