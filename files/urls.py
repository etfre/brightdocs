from django.conf.urls import patterns, url

from files import views

urlpatterns = patterns('',
    url(r'^upload/?$', views.upload_view, name='logout'),
)