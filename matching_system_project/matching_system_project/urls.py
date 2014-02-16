from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'matching_system_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    # @TODO make this url work for single worlds
    url(r'^projects/(?P<project_name_url>\w+)/$', views.project, name='project'),  # New!
    #url(r'projects/', views.projects, name='projects'),

)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )
