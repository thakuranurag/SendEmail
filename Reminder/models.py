from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserData(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=120)
	mobile=models.IntegerField()
	date=models.DateField()

