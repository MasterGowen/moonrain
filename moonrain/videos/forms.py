from django import forms
from suit_redactor.widgets import RedactorWidget
from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'videofile', 'comments', 'lang', 'tags', 'project']
        widgets = {
            'comments': RedactorWidget(editor_options={'lang': 'ru'})
        }