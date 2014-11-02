from django.contrib import admin
from .models import Project
from .forms import ProjectForm


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('name', 'author', 'date', 'Комментарий', 'users')

admin.site.register(Project, ProjectAdmin)