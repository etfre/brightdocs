from django.conf.urls import patterns, url

from ui import views
import files

urlpatterns = patterns('',
	url(r'^$', views.default_view, name='default'),
    url(r'^home$', views.home, name='home'),
    url(r'^blueprint/\d+$', views.blueprint_view, name='blueprint'),
    # url(r'^new/trigger/$', views.new_trigger, name='trigger'),
    url(r'^register/?$', views.registration_page, name='registration'),
    url(r'^submit/registration/?$', views.register, name='submit_registration'),
    url(r'^submit/login/?$', views.login, name='submit_login'),
    url(r'^logout/?$', views.logout_view, name='logout'),


    url(r'^new/blueprint/?$', views.new_blueprint_view, name='blueprint'),
)