from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('ui.urls')),
    url(r'^files/', include('files.urls')),
    url(r'^admin/', include(admin.site.urls)),
)