from django.contrib import admin
from moonrain.videos.models import Video, VideoAdmin

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)

