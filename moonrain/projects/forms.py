from django import forms
from suit_redactor.widgets import RedactorWidget
from .models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'comments', 'tags', 'permission']
        widgets = {
            'comments': RedactorWidget(editor_options={'lang': 'ru'})
        }