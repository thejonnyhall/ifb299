from django.conf.urls import include, url
from django.conf import settings
from django.contrib.auth import *
from . import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout')

]
