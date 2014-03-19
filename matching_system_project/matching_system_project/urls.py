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
    url(r'^projects/add_position/$', views.add_position, name='add_position'), # alina forms
    url(r'^projects/(?P<project_name_url>\w+)/$', views.project, name='project'),  # New!
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^applist/$', views.applist, name = 'applist'),
    url(r'^apply/(?P<uid>[-\w]+)/(?P<posid>[-\w]+)/$', views.apply, name = 'apply'),



)
#
# if settings.DEBUG:
#     urlpatterns += patterns(
#         'django.views.static',
#         (r'media/(?P<path>.*)',
#          'serve',
#          {'document_root': settings.MEDIA_ROOT}), )

