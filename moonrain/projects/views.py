import json
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from .models import Project
from ..videos.models import Video, VideosSequence
from ..videos.views import new_sequence, get_sequence
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.context_processors import csrf
from .forms import ProjectForm


def projects_list_all(request):
    projects = []

    for project in Project.objects.all():
        if project.permission == 'public':
            projects.append(project)

        @login_required
        def for_users(request, project, projects):
            if project.permission == 'for_users':
                projects.append(project)
        for_users(request, project, projects)

        @login_required
        def for_staff(request, project, projects):
            if project.permission == 'for_staff':
                if request.user == project.author or str(request.user) in str(project.users()):
                    projects.append(project)
        for_staff(request, project, projects)

    projects = list(reversed(projects))

    paginator = Paginator(projects, 10)
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)

    return render(request, 'projects/index.html', {'projects': projects, 'pages': range(1, (paginator.num_pages + 1))})


def detail(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
        jsonSequence = json.loads(get_sequence(request, project))
    except ObjectDoesNotExist:
        raise Http404

    videos_ids = jsonSequence['sequence'].split(',')
    videos = []

    for video_id in videos_ids:
        if video_id != 'None':
            video = Video.objects.get(id=video_id)
            videos.append(video)


    if project.permission == 'public':
        return render(request, 'projects/project.html', {'project': project, 'videos': videos})
    elif project.permission == 'for_users' \
            and request.user:
        return render(request, 'projects/project.html', {'project': project, 'videos': videos})
    elif project.permission == 'for_staff' \
            and request.user == project.author \
            or str(request.user) \
                    in str(project.users()):
        return render(request, 'projects/project.html', {'project': project, 'videos': videos})
    else:
        return HttpResponse(status=403)


def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author_id = request.user.id
            project.save()
            new_sequence(request, project.id)
            return redirect(project)
    args = {}
    args.update(csrf(request))
    args['form'] = ProjectForm()
    return render(request, 'projects/new.html', args)


class ProjectDelete(DeleteView):
    model = Project
    fields = []
    success_url = '/projects/'


class ProjectUpdate(UpdateView):
    model = Project
    fields = ['name', 'comments', 'tags', 'permission']