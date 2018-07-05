# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib import admin
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.validators import FileExtensionValidator

from apps import OverwriteStorage
import os

DEFAULT_LENGTH = 50

# Create your models here.
@python_2_unicode_compatible
class Stuff(models.Model):  #Staff Account
    user = models.OneToOneField(User, verbose_name=_("用户"))
    hospital = models.CharField(_("医院"),max_length=DEFAULT_LENGTH, blank=True)
    phone = models.CharField(_("电话号码"),max_length=DEFAULT_LENGTH, blank=True)
    home_work_phone = models.CharField(_("座机"),max_length=DEFAULT_LENGTH, blank=True)

    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name = '工作人员'
        verbose_name_plural = '工作人员'

@python_2_unicode_compatible
class Doctor(models.Model):
    first_name = models.CharField(_('姓氏'), max_length=DEFAULT_LENGTH, blank=True)
    last_name = models.CharField(_('名'), max_length=DEFAULT_LENGTH, blank=True)
    avatar = models.FileField(_('个人资料图片'), upload_to='uploads/doctoravatar', blank = True)
    description = models.TextField(_('描述'), blank=True)
    doctor_type = models.CharField(_('医生类型'), max_length=DEFAULT_LENGTH, choices=(('huizon', 'huizon'),('jiuyi', 'jiuyi')),
                                      default='huizon')
    def __str__(self):
        return str(self.first_name)
    
    class Meta:
        verbose_name = '医生'
        verbose_name_plural = '医生'

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'description',)

@python_2_unicode_compatible
class Patient(models.Model):
    first_name = models.CharField(_('姓氏'),max_length=DEFAULT_LENGTH, blank=True)
    last_name = models.CharField(_('名'), max_length=DEFAULT_LENGTH, blank=True)
    email = models.EmailField(_('邮箱'), max_length=DEFAULT_LENGTH, blank=True)
    phonenumber = models.CharField(_('病人电话'), max_length=DEFAULT_LENGTH)
    password = models.CharField(_('password'), max_length=255)
    chujonservice = models.BooleanField(_('出诊服务'), blank=True, default=False) #0: Not Purchase, 1: Purchase
    huijonservice = models.BooleanField(_('会诊服务'), blank=True, default=False) #0: Not Purchase, 1: Purchase
    jiuyiservice = models.BooleanField(_('就一服务'), blank=True, default=False) #0: Not Purchase, 1: Purchase
    verifycode = models.CharField(max_length=DEFAULT_LENGTH, blank=True)
    
    def __str__(self):
        return str(self.phonenumber)
    
    class Meta:
        verbose_name = '病人'
        verbose_name_plural = '病人'

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phonenumber', 'chujonservice', 'huijonservice', 'jiuyiservice')

@python_2_unicode_compatible
class MedicalHistory(models.Model):

    staff = models.ForeignKey(Stuff, on_delete=models.CASCADE)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    height = models.CharField(_('身高'), max_length=DEFAULT_LENGTH, blank=True)
    weight = models.CharField(_('体重'), max_length=DEFAULT_LENGTH, blank=True)
    bloodtype = models.CharField(_('血型'),max_length=DEFAULT_LENGTH, choices=(
        ('o', 'O'), ('a', 'A'), ('ab', 'AB'), ('b', 'B')))
    smoke = models.BooleanField(_('抽烟'),blank=True, default=False)
    wine = models.BooleanField(_('饮酒'),blank=True, default=False)

    creation_date = models.DateTimeField(_('创建时间'),default=timezone.now, blank=True)

    def __str__(self):
        return str(self.patient)

class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('patient_firstname', 'height', 'weight', 'bloodtype', 'smoke', 'wine', 'creation_date')

    def patient_firstname(self, instance):
        return instance.patient.first_name

@python_2_unicode_compatible
class MedicalHistoryExcel(models.Model):
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE,verbose_name = _('工作人员'))
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,verbose_name = _('病人'))

    excel = models.FileField(_("医疗excel"),upload_to='uploads/excel/medical', blank = True, validators=[FileExtensionValidator(['xlsx','xls'])])

    image1 = models.FileField(_("图片1"), upload_to='uploads/image1/medical', blank = True, validators=[FileExtensionValidator(['png','jpeg','jpg'])])
    image2 = models.FileField(_("图片2"), upload_to='uploads/image2/medical', blank = True, validators=[FileExtensionValidator(['png','jpeg','jpg'])])
    
    video1 = models.FileField(_("视频"),upload_to='uploads/video1/medical', blank = True, validators=[FileExtensionValidator(['mpg','avi','mp4'])])
    creation_date = models.DateTimeField(_('创建时间'), default=timezone.now, blank=True)

    def __str__(self):
        return str(self.patient)

    class Meta:
        verbose_name = '医疗excel'
        verbose_name_plural = '医疗excel'

class MedicalHistoryExcelAdmin(admin.ModelAdmin):
    list_display = ('stuff_firstname', 'patient_phonenumber')

    def stuff_firstname(self, instance):
        return instance.stuff.user
    def patient_phonenumber(self, instance):
        return instance.patient.phonenumber

@python_2_unicode_compatible
class MedicalHistoryExcelTemplate(models.Model):
    excel = models.FileField(upload_to='uploads/excel/medicaltemplate', blank = True, validators=[FileExtensionValidator(['xlsx','xls'])])
    def __str__(self):
        return str(self.excel)

    class Meta:
        verbose_name = '医疗excel模版'
        verbose_name_plural = '医疗excel模版'

@python_2_unicode_compatible
class MedicineHistoryExcel(models.Model):
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE,verbose_name = _('工作人员'))
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,verbose_name = _('病人'))

    excel = models.FileField(_("治疗excel"),upload_to='uploads/excel/medicine', blank = True, validators=[FileExtensionValidator(['xlsx','xls'])])

    image1 = models.FileField(_("图片1"),upload_to='uploads/image1/medicine', blank = True, validators=[FileExtensionValidator(['png','jpeg','jpg'])])
    image2 = models.FileField(_("图片2"),upload_to='uploads/image2/medicine', blank = True, validators=[FileExtensionValidator(['png','jpeg','jpg'])])
    
    video1 = models.FileField(_("视频"),upload_to='uploads/video1/medicine', blank = True, validators=[FileExtensionValidator(['mpg','avi','mp4'])])
    creation_date = models.DateTimeField(_('创建时间'), default=timezone.now, blank=True)

    def __str__(self):
        return str(self.patient)

    class Meta:
        verbose_name = '治疗excel'
        verbose_name_plural = '治疗excel'

class MedicineHistoryExcelAdmin(admin.ModelAdmin):
    list_display = ('stuff_firstname', 'patient_phonenumber')

    def stuff_firstname(self, instance):
        return instance.stuff.user
    def patient_phonenumber(self, instance):
        return instance.patient.phonenumber

@python_2_unicode_compatible
class MedicineHistoryExcelTemplate(models.Model):
    excel = models.FileField(upload_to='uploads/excel/medicinetemplate', blank = True, validators=[FileExtensionValidator(['xlsx', 'xls'])])
    def __str__(self):
        return str(self.excel)
    class Meta:
        verbose_name = '治疗excel模版'
        verbose_name_plural = '治疗excel模版'

@python_2_unicode_compatible
class TreatmentHistoryExcel(models.Model):
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE, verbose_name = _('工作人员'))
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name = _('病人'))

    excel = models.FileField(_("病历excel"), upload_to='uploads/excel/treatment', blank = True, validators=[FileExtensionValidator(['xlsx', 'xls'])])

    image1 = models.FileField(_("图片1"), upload_to='uploads/image1/treatment', blank = True, validators=[FileExtensionValidator(['png','jpeg','jpg'])])
    image2 = models.FileField(_("图片2"), upload_to='uploads/image2/treatment', blank = True, validators=[FileExtensionValidator(['png','jpeg','jpg'])])
    
    video1 = models.FileField(_("视频"),upload_to='uploads/video1/treatment', blank = True, validators=[FileExtensionValidator(['mpg','avi','mp4'])])
    creation_date = models.DateTimeField(_('创建时间'),default=timezone.now, blank=True)

    def __str__(self):
        return str(self.patient)

    class Meta:
        verbose_name = '病历excel'
        verbose_name_plural = '病历excel'

class TreatmentHistoryExcelAdmin(admin.ModelAdmin):
    list_display = ('stuff_firstname', 'patient_phonenumber')

    def stuff_firstname(self, instance):
        return instance.stuff.user
    def patient_phonenumber(self, instance):
        return instance.patient.phonenumber

@python_2_unicode_compatible
class TreatmentHistoryExcelTemplate(models.Model):
    excel = models.FileField(upload_to='uploads/excel/treatmenttemplate', blank = True, validators=[FileExtensionValidator(['xlsx','xls'])])
    def __str__(self):
        return str(self.excel)
    class Meta:
        verbose_name = '病历excel模版'
        verbose_name_plural = '病历excel模版'

class ReferralHistory(models.Model):
    phonenumber = models.CharField(_('电话号码'),max_length=DEFAULT_LENGTH)
    verifycode = models.CharField(_('邀请码'),max_length=DEFAULT_LENGTH, blank=True)
    
    def __str__(self):
        return str(self.phonenumber)
    
    class Meta:
        verbose_name = '邀请模版'
        verbose_name_plural = '邀请模版'

@python_2_unicode_compatible
class DiseaseType(models.Model):
    diseasetype = models.CharField(_('diseasetype'), max_length=DEFAULT_LENGTH,blank=True)
        
    def __str__(self):
        return str(self.diseasetype)

    class Meta:
        verbose_name = '疾病类型'
        verbose_name_plural = '疾病类型'

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.pdf" % (instance.disease_type.diseasetype)
    return os.path.join('uploads/pdf', filename)

class PdfTemplate(models.Model):
    disease_type = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)
    pdf = models.FileField(max_length = DEFAULT_LENGTH, upload_to=content_file_name, storage=OverwriteStorage(), validators=[FileExtensionValidator(['pdf'])])
    def __str__(self):
        return str(self.disease_type)
    class Meta:
        verbose_name = 'pdf模版'
        verbose_name_plural = 'pdf模版'
