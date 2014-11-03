from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from .videos import views as vidviews
from .projects import views as projviews

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^videos/', vidviews.video_list),
                       url(r'^$', projviews.projects_list_all, name='all_projects')

)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )


#AA
urlpatterns += patterns('',
                        url(r'^login/', 'django.contrib.auth.views.login', { "template_name": "accounts/login.html" }),
                        url(r'logout', 'django.contrib.auth.views.logout')
                        )