from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from .videos import views as vidviews
from .projects import views as projviews
from .accounts import views as accviews
import moonrain.views

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^videos/$', vidviews.video_list),
                       url(r'^videos/(?P<pk>\d+)/$', vidviews.video_detail),
                       url(r'^videos/(?P<pk>\d+)/delete/$', vidviews.VideoDelete.as_view()),
                       url(r'^videos/(?P<pk>\d+)/update/$', vidviews.VideoUpdate.as_view()),
                       url(r'^videos/new/$', vidviews.new_video),
                       url(r'^$', projviews.projects_list_all, name='all_projects'),
                       url(r'^projects/$', projviews.projects_list_all, name='all_projects'),
                       url(r'^projects/(?P<project_id>\d+)/$', projviews.detail),
                       url(r'^projects/new/$', projviews.new_project),
                       url(r'^projects/(?P<pk>\d+)/delete/$', projviews.ProjectDelete.as_view()),
                       url(r'^projects/(?P<pk>\d+)/update/$', projviews.ProjectUpdate.as_view()),
                       url(r'^projects/(?P<project_id>\d+)/add/$', vidviews.new_video, name='new_video'),
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
                        url(r'^register/', accviews.register_user),
                        )

#comments

urlpatterns += patterns('',
                        url(r'^project/comments/', include('fluent_comments.urls')),
                        )

# media FOR TESTING!

urlpatterns += patterns('',
                        url(r'^data/(?P<path>.*)$', 'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT}))


handler403 = 'views.moon_403'
handler404 = 'moon_404'
handler500 = 'moonrain.views.moon_500'
