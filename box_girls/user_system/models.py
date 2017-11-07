# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from questions.models import TextQuestion

GENDER = (
	('m', 'male'),
	('f', 'female')
)


class Guardian(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True) 

class MembershipRegistration(models.Model):
	# user = models.OneToOneField(User)

	name = models.CharField(max_length=255, blank=True, null=True)
	picture = models.ImageField(blank=True, null=True)
	DOB = models.DateField(blank=True, null=True)
	gender = models.CharField(max_length=20, choices=GENDER)
	parents = models.ForeignKey(Guardian, blank=True, null=True)
	contact_number = models.CharField(max_length=20, blank=True, null=True)
	area_of_residence = models.CharField(max_length=255, blank=True, null=True)
	physical_address = models.CharField(max_length=255, blank=True, null=True)
	name_of_school = models.CharField(max_length=255, blank=True, null=True)
	questions = models.ManyToManyField(TextQuestion, blank=True)

"""
    • In School or out of school
    • Other things you can do for box girls other than boxing
    • List of hobbies
"""