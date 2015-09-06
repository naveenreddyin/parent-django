__author__ = 'naveenkumarvasudevan'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'registration.views',
    url(r'^register-parent-app/(?P<phone_no>\d+)$',
        'register_parent_app',
        name='register_parent_app'),
    url(r'^connect-app/(?P<child_no>\d+)/(?P<parent_no>\d+)$',
        'connect_app_register',
        name='connect-app'),
)
