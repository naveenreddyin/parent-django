__author__ = 'naveenkumarvasudevan'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'generator.views',
    url(r'^get-token/$',
        'generate_token',
        name='generate_token'),
)
