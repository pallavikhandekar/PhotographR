from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^FlickerUI/', 'FlickerUI.views.search'),
                       url(r'^FlickerUI/index/', 'FlickerUI.views.index'),)
