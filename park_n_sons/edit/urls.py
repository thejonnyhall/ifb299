from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.edit, name='edit'),
    url(r'^([0-9]+)/$', views.display, name='display'),
    url(r'^([0-9]+)/add/$', views.add, name='add'),
    url(r'^([0-9]+)/modify/([0-9]+)/$', views.modify, name='modify'),
    url(r'^([0-9]+)/delete/([0-9]+)/$', views.delete, name='delete')
]