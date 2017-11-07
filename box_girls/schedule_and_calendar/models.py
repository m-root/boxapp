# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from questions.models import TextQuestion


class ActivityScheduleAndCalendar(models.Model):
    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank=True)
    from_time = models.TimeField(blank=True)
    to_time = models.TimeField(blank=True)
    activity = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    assigned_to = models.CharField(max_length=255, blank=True, null=True)
    activities  = models.CharField(max_length=255, blank=True, null=True)
    target_group = models.CharField(max_length=255, blank=True, null=True)
    course_outline = models.CharField(max_length=255, blank=True, null=True)
    location  = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
