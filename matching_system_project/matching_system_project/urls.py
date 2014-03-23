from django.conf.urls import patterns, include, url
from django.contrib import admin

import views


admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.index, name='index'),
                       # @TODO make this url work for single worlds
                       url(r'^projects/add_project/$', views.add_project,
                           name='add_project'),  # alina forms
                       url(r'^projects/add_position/$', views.add_position,
                           name='add_position'),  # alina forms
                       url(r'^projects/(?P<project_name_url>\w+)/$',
                           views.project, name='project'),  # New!


                       url(r'^register/$', views.register, name='register'),
                       # ADD NEW PATTERN!
                       url(r'^login/$', views.user_login, name='login'),


                       url(r'^restricted/', views.restricted,
                           name='restricted'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^applist/$', views.applist, name='applist'),
                       url(r'^pm-projects/$', views.pmprojects,
                           name='pm-projects'),
                       url(r'^history/$', views.history, name='history'),
                       url(r'^apply/(?P<uid>[-\w]+)/(?P<posid>[-\w]+)/$',
                           views.apply, name='apply'),
                       url(r'^accept/(?P<appid>[-\w]+)/$', views.accept,
                           name='accept'),


)
