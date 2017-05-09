from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserData(models.Model):
	name=models.CharField(max_length=100,null=True,blank=True)
	email=models.EmailField(max_length=120,null=True,blank=True)
	phone=models.IntegerField(null=True,blank=True)
	date=models.DateField(null=True,blank=True)

