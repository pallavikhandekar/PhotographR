from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^PhotographeR/', 'FlickerUI.views.search'),
                       (r'^index/$', 'FlickerUI.views.getallphotos'),
                       (r'^similarSearch/$', 'FlickerUI.views.similarsearch'),)
