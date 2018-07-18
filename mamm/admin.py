# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Stuff, MedicalHistory, MedicalHistoryAdmin, Patient, PatientAdmin, MedicalHistoryExcel, MedicalHistoryExcelAdmin, MedicalHistoryExcelTemplate, Doctor, DoctorAdmin
from .models import MedicineHistoryExcel, MedicineHistoryExcelAdmin, MedicineHistoryExcelTemplate
from .models import TreatmentHistoryExcel, TreatmentHistoryExcelAdmin, TreatmentHistoryExcelTemplate
from .models import ReferralHistory
from .models import PdfTemplate
from .models import DiseaseType
from .models import TextImageTemplate

admin.site.register(Stuff)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(MedicalHistoryExcel, MedicalHistoryExcelAdmin)
admin.site.register(MedicalHistoryExcelTemplate)
admin.site.register(MedicineHistoryExcel, MedicineHistoryExcelAdmin)
admin.site.register(MedicineHistoryExcelTemplate)
admin.site.register(TreatmentHistoryExcel, TreatmentHistoryExcelAdmin)
admin.site.register(TreatmentHistoryExcelTemplate)
admin.site.register(ReferralHistory)
admin.site.register(PdfTemplate)
admin.site.register(DiseaseType)
admin.site.register(TextImageTemplate, )
admin.site.site_header = _('Medical administration')
admin.site.site_title = _('Medical administration')
admin.site.index_title = _('Medical administration')
