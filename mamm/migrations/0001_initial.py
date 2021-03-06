# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-27 10:31
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('avatar', models.FileField(blank=True, upload_to='uploads/doctoravatar')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(blank=True, max_length=50)),
                ('weight', models.CharField(blank=True, max_length=50)),
                ('bloodtype', models.CharField(choices=[('o', 'O'), ('a', 'A'), ('ab', 'AB'), ('b', 'B')], max_length=50)),
                ('smoke', models.BooleanField(default=False)),
                ('wine', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistoryExcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel', models.FileField(blank=True, upload_to='uploads/excel', validators=[django.core.validators.FileExtensionValidator(['xlsx'])])),
                ('image1', models.FileField(blank=True, upload_to='uploads/image1', validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg'])])),
                ('image2', models.FileField(blank=True, upload_to='uploads/image2', validators=[django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg'])])),
                ('video1', models.FileField(blank=True, upload_to='uploads/video1', validators=[django.core.validators.FileExtensionValidator(['mpg', 'avi', 'mp4'])])),
                ('creation_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistoryExcelTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel', models.FileField(blank=True, upload_to='uploads/excel', validators=[django.core.validators.FileExtensionValidator(['xlsx'])])),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('phonenumber', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(max_length=255, verbose_name='password')),
                ('chujonservice', models.BooleanField(default=False)),
                ('huijonservice', models.BooleanField(default=False)),
                ('jiuyiservice', models.BooleanField(default=False)),
                ('verifycode', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PatientOnlyPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.CharField(blank=True, max_length=50)),
                ('chujonservice', models.BooleanField(default=False)),
                ('huijonservice', models.BooleanField(default=False)),
                ('jiuyiservice', models.BooleanField(default=False)),
                ('verifycode', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('home_work_phone', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='medicalhistoryexcel',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mamm.Patient'),
        ),
        migrations.AddField(
            model_name='medicalhistoryexcel',
            name='stuff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mamm.Stuff'),
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mamm.Patient'),
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mamm.Stuff'),
        ),
    ]
