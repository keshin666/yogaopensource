# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-13 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
