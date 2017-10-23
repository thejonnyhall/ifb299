from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^maps/', views.mapscrape, name='mapscrape'),
]