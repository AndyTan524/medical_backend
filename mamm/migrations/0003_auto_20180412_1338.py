# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-12 13:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mamm', '0002_auto_20180412_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalhistoryexcel',
            name='video1',
            field=models.FileField(blank=True, upload_to='uploads/video1', validators=[django.core.validators.FileExtensionValidator(['mpg', 'avi', 'mp4'])]),
        ),
    ]
