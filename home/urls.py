from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import reverse
#from django.conf.urls import patterns, include
admin.autodiscover()

from home import views

app_name='home_app'
urlpatterns = [
	url(r'', (views.auth_home), name = 'home_page',),
]