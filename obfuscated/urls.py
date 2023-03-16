"""obfuscated URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from url_obfuscated.helpers import generate_url_pattern
from django.urls import re_path as url
from .views import *

# urlpatterns = ['views',
urlpatterns = [
    url(generate_url_pattern('/'), home, name='home'),
    url(generate_url_pattern('obfuscated_link', params=['(?P<name>[^/]+)']), obfuscated_link, name='obfuscated_link'),
    url(generate_url_pattern('optional_param', params=['(?:(?P<param>[^/]+)/)?']), optional_param, name='optional_param'),
]
