from django.contrib import admin
from .models import Project
from .forms import ProjectForm
from taggit.models import Tag


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('name', 'author', 'date', 'Комментарий', 'users')

admin.site.register(Project, ProjectAdmin)
admin.site.unregister(Tag)