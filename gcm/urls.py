__author__ = 'naveenkumarvasudevan'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'gcm.views',
    url(r'^$',
        'send_push',
        name='send_push'),
)
