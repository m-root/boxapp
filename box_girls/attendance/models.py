# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from questions.models import TextQuestion

class Attendance(models.Model):
	activity_name = models.CharField(max_length=255, blank=True, null=True)
	activity_objective = models.CharField(max_length=255, blank=True, null=True)
	other_activity = models.CharField(max_length=255, blank=True, null=True)
	name_attendance = models.CharField(max_length=255, blank=True, null=True)