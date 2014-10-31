from django.contrib import admin
from moonrain.projects.models import Project, ProjectAdmin

admin.site.register(Project, ProjectAdmin)