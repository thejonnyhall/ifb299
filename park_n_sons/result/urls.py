from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.result, name='result'),
    url(r'^([0-9]+)/', views.item, name='item'),
]