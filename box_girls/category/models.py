# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from questions.models import TextQuestion


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
