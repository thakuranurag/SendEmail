# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reminder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
