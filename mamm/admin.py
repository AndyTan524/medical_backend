# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import Stuff, MedicalHistory, MedicalHistoryAdmin, Patient, PatientAdmin, MedicalHistoryExcel, MedicalHistoryExcelAdmin, MedicalHistoryExcelTemplate, Doctor, DoctorAdmin

admin.site.register(Stuff)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(MedicalHistoryExcel, MedicalHistoryExcelAdmin)
admin.site.register(MedicalHistoryExcelTemplate)
admin.site.site_header = 'MEDICAL Administration'
admin.site.site_title = 'MEDICAL Administration'
admin.site.index_title = 'MEDICAL Administration'
