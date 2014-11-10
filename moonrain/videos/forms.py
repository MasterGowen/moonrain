from django import forms
from suit_redactor.widgets import RedactorWidget
from .models import Video
from django.contrib import admin


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'videofile', 'comments', 'lang', 'tags']
        widgets = {
            'comments': RedactorWidget(editor_options={'lang': 'ru'})
        }


class VideoAdmin(admin.ModelAdmin):
    form = VideoForm
    list_display = ('name', 'project', 'date', 'url', 'author', 'resolution', 'duration', 'Комментарий')
    readonly_fields = ('parent',)