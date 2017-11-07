# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from questions.models import TextQuestion


COLOR = (
    ('RD','Red'),
    ('YE','Yellow'),
    ('BL','Blue'),
)


class Notification(models.Model):
    activity = models.CharField(max_length=255, blank=True, null=True, choices=COLOR)
