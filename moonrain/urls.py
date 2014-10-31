from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from .videos import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^videos/', views.video_list),

)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )