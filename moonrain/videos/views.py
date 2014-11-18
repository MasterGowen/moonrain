from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.views.generic.edit import UpdateView, DeleteView
from django.core.context_processors import csrf
from .models import Video
from .forms import VideoForm
from ..projects.models import Project


@login_required
def video_list(request):

    videos = Video.objects.filter(author=request.user)

    paginator = Paginator(videos, 10)
    page = request.GET.get('page')

    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    return render(request, 'videos/index.html', {'videos': videos, 'pages': range(1, (paginator.num_pages + 1))})


def video_detail(request, pk):
    try:
        video = Video.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404
    if video.project:
        project = video.project
        if project.permission == 'public':
            return render(request, 'videos/video.html', {'video': video})
        elif project.permission == 'for_users' \
                and request.user:
            return render(request, 'videos/video.html', {'video': video})
        elif project.permission == 'for_staff' \
                and request.user == project.author \
                or str(request.user) in str(project.users()):
            return render(request, 'videos/video.html', {'video': video})
        else:
            return HttpResponse(status=403)
    else:
        if video.author == request.user:
            return render(request, 'videos/video.html', {'video': video})
        else:
            return HttpResponse(status=403)


def new_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            video = form.save()
            return redirect(video)
    args = {}
    args.update(csrf(request))
    args['form'] = VideoForm()
    return render(request, 'videos/new.html', args)


def add_video(request, pk):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.author = request.user
            print(Project.objects.filter(pk=pk))
            video.project = Project.objects.filter(pk=pk)
            video = form.save()
            return redirect(video)
    args = {}
    args.update(csrf(request))
    args['form'] = VideoForm()
    return render(request, 'videos/new.html', args)


class VideoDelete(DeleteView):
    model = Video
    fields = []
    success_url = '/videos'


class VideoUpdate(UpdateView):
    model = Video
    fields = ['name', 'videofile', 'comments', 'lang', 'tags']