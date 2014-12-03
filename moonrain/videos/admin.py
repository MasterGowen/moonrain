from django.contrib import admin
from moonrain.videos.forms import Video, VideoForm

class VideoAdmin(admin.ModelAdmin):

    def save_model(self, request, new_object, form, change):
        new_object.author = request.user
        new_object.save()

    form = VideoForm
    list_display = ('name', 'project', 'date', 'url', 'author', 'resolution', 'duration', 'Комментарий')
    readonly_fields = ('parent', )

admin.site.register(Video, VideoAdmin)
