from django.shortcuts import render
from .models import Project
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required


def projects_list_all(request):
    projects = []

    for project in Project.objects.all():
        if project.permission == 'public':
            projects.append(project)

    @login_required
    def for_users(request):
        for project in Project.objects.all():
            if project.permission == 'for_users':
                projects.append(project)

    @login_required
    def for_staff(request):
        for project in Project.objects.all():
            if project.permission == 'for_staff':
                if request.user == project.author or str(request.user) in str(project.users()):
                    projects.append(project)
    for_staff(request)
    for_users(request)

    projects = {'projects': projects}

    return render(request, 'projects/index.html', projects)