# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-24 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mamm', '0005_remove_patient_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]
