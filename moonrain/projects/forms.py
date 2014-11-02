from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget


class ProjectForm(ModelForm):
    class Meta:
        widgets = {
            'comments': RedactorWidget(editor_options={'lang': 'ru'})
        }
