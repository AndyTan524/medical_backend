"""medical_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from django.views import static
from django.conf.urls.i18n import i18n_patterns


from rest_framework import routers
from rest_framework.authtoken import views

from mamm import views as mamm_views
import settings

urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^', include('mamm.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/media/(?P<path>.*)$', static.serve, {'document_root' : settings.MEDIA_ROOT}),
    prefix_default_language=False

)

