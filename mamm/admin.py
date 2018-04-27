# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


# from .models import Person, Broker, TradingAccount, Instrument, GlobalTrade, Setting
from .models import Stuff, MedicalHistory, MedicalHistoryAdmin, Patient, PatientAdmin, MedicalHistoryExcel, MedicalHistoryExcelAdmin, MedicalHistoryExcelTemplate, Doctor, DoctorAdmin


admin.site.register(Stuff)
# admin.site.register(MedicalHistory, MedicalHistoryAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(MedicalHistoryExcel, MedicalHistoryExcelAdmin)
admin.site.register(MedicalHistoryExcelTemplate)
admin.site.site_header = 'MEDICAL Administration'
admin.site.site_title = 'MEDICAL Administration'
admin.site.index_title = 'MEDICAL Administration'
# admin.site.register(Broker, )
# admin.site.register(TradingAccount, )
# admin.site.register(Instrument, )
# admin.site.register(GlobalTrade, )
# admin.site.register(Setting, )
# admin_site = MyAdminSite()