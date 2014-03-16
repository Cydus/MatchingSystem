from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    # @TODO make this url work for single worlds
    url(r'^projects/add_project/$', views.add_project, name='add_project'), # alina forms
    url(r'^projects/(?P<project_name_url>\w+)/$', views.project, name='project'),  # New!
)
#
# if settings.DEBUG:
#     urlpatterns += patterns(
#         'django.views.static',
#         (r'media/(?P<path>.*)',
#          'serve',
#          {'document_root': settings.MEDIA_ROOT}), )

