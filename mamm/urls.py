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
    url(r'^api/medicalhistory/', views.getmedicalhistory),
    url(r'^api/forgotpass/', views.forgotpass),
    url(r'^api/verifycode/', views.verifycode),
    url(r'^api/setpass/', views.setpass),
]

urlpatterns = format_suffix_patterns(urlpatterns)
