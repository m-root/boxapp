from django.db import models

# Create your models here.
class TextQuestion(models.Model):
	question = models.TextField(blank=True, null=True)
	answer = models.TextField(null=True, blank=True)