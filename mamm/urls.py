from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'mamm'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^api/login/', views.login),
	url(r'^api/loginphone/', views.loginphone),
	url(r'^api/verifyphonelogin/', views.verifycode_phone),
	url(r'^api/register/', views.register),
	url(r'^api/chujonservice/', views.chuzonservice),
	# Forgot Password
	url(r'^api/forgotpass/', views.forgotpass),
	url(r'^api/verifycode/', views.verifycode),
	url(r'^api/setpass/', views.setpass),

	# Get medical History 
	url(r'^api/medicalhistory/', views.getmedicalhistory), #chujon
	url(r'^api/medicinehistory/', views.getmedicinehistory), #huijon
	url(r'^api/treathistory/', views.gettreatmenthistory), #jiuyi

	# Get Doctor
	url(r'^api/doctors/', views.getdoctors),

	# Send Verify Code on the Admin, Stuff, Doctor, Patient(Already Created)
	url(r'^api/referral/sendverifycode', views.sendvcode_referral),
	
	# 
	url(r'^api/pdftemplate', views.getpdftemplate),
]

urlpatterns = format_suffix_patterns(urlpatterns)
