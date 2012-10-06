from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': "home.html"}),
    url(r'^v1/$', 'ordrin.views.ajax_sightings'),

    url(r'^admin/', include(admin.site.urls)),
)
