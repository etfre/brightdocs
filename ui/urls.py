from django.conf.urls import patterns, url

from ui import views

urlpatterns = patterns('',
	url(r'^/?$', views.default_view, name='default'),
    url(r'^home$', views.home, name='home'),
    url(r'^login/?$', views.login_page, name='login'),
    url(r'^blueprint/?$', views.new_blueprint, name='blueprint'),
    url(r'^register/?$', views.registration_page, name='registration'),
    url(r'^submit/registration/?$', views.register, name='submit_registration'),
    url(r'^submit/login/?$', views.login, name='submit_login'),
    url(r'^logout/?$', views.logout_view, name='logout'),
)