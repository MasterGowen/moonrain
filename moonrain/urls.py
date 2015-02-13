from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from .projects.views import ProjectUpdate, ProjectDelete
from .videos.views import VideoDelete, VideoUpdate

urlpatterns = patterns('moonrain.videos',
  url(r'^videos/$', 'views.video_list'),
  url(r'^videos/(?P<pk>\d+)/$', 'views.video_detail'),
  url(r'^videos/new/$', 'views.new_video'),
  url(r'^projects/(\d+)/add/$', 'views.new_video', name='new_video'),
  url(r'^ajaxUpdateSequence/$', 'views.update_sequence'),
  )

urlpatterns += patterns('', 
  url(r'^videos/(?P<pk>\d+)/delete/$', VideoDelete.as_view()),
  url(r'^videos/(?P<pk>\d+)/update/$', VideoUpdate.as_view()),)

urlpatterns += patterns('moonrain.projects',
  url(r'^$', 'views.projects_list_all', name='all_projects'),
  url(r'^projects/$', 'views.projects_list_all', name='all_projects'),
  url(r'^projects/(?P<project_id>\d+)/$', 'views.detail'),
  url(r'^projects/new/$', 'views.new_project'),
  )

urlpatterns += patterns('',
  url(r'^projects/(?P<pk>\d+)/delete/$', ProjectDelete.as_view()),
  url(r'^projects/(?P<pk>\d+)/update/$', ProjectUpdate.as_view()),)

urlpatterns += patterns('moonrain.accounts',
  url(r'^register/', 'views.register_user'),
  )

urlpatterns += patterns('',
     url(r'^admin/', include(admin.site.urls)),
  )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )


#AA
urlpatterns += patterns('',
                        url(r'^login/', 'django.contrib.auth.views.login', {"template_name": "accounts/login.html"}),
                        url(r'logout/', 'django.contrib.auth.views.logout'),
                        )

#comments

urlpatterns += patterns('',
                        url(r'^project/comments/', include('fluent_comments.urls')),
                        )

# media FOR TESTING!

urlpatterns += patterns('',
                        url(r'^data/(?P<path>.*)$', 'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT}))

