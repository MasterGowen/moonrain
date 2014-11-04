from django.shortcuts import render, render_to_response
from .models import Project
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

# test section
from django.http import HttpResponse


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


def detail(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('projects/project.html', {'project': project})