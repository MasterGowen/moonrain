import os
import json
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.views.generic.edit import UpdateView, DeleteView
from django.core.context_processors import csrf
from pymediainfo import MediaInfo
from .models import Video, VideosSequence
from .forms import VideoForm
from ..projects.models import Project


def analysis(video):
    mediainfoobject = MediaInfo.parse(str(settings.BASE_DIR) + str(os.path.normpath(video.videofile.url)))
    try:    
        for track in mediainfoobject.tracks:
            if track.track_type == 'General':
                video.format = track.format
                video.filesize = track.file_size
                video.duration = track.duration
            if track.track_type == 'Video':
                video.width = track.width
                video.height = track.height
                video.resolution = str(video.width) + 'x' + str(video.height)
                video.vcodec = track.codec
                video.aspect = track.display_aspect_ratio
                video.framerate = track.frame_rate
                video.colorspace = track.color_space
                video.bitdepth = track.bit_depth
                video.vbitrate = track.bit_rate
            if track.track_type == 'Audio':
                video.acodec = track.format
                video.abitrate = track.bit_rate
                video.asamplingrate = track.asampling_rate
                video.abitdepth = track.bit_depth
                video.channels = track.channel_s
    except:
        return video


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


def new_video(request, project_id):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():



            video = form.save(commit=False)
            video.author = request.user

            try:
                video.project = Project.objects.get(id=project_id)
            except:
                video.project = None

            video = analysis(video)
            video.save()
            
            jsonSequence = json.loads(get_sequence(request, video.project))
            videos = jsonSequence['sequence']

            if videos == 'None' or videos is None:
                videos = str(video.id)
                is_first = True
            else:
                videos = str(videos) + ',' + str(video.id)
                is_first = False

            update_sequence(request, video.project, videos, is_first, is_new=True)

            try:
                return redirect(video.project)
                pass
            except:
                video.save()
                return redirect(video)
    args = {}
    args.update(csrf(request))
    args.update({"project_id": project_id})
    args['form'] = VideoForm()
    return render(request, 'videos/new.html', args)


class VideoDelete(DeleteView):
    model = Video
    fields = []
    success_url = '/videos'


class VideoUpdate(UpdateView):
    model = Video
    fields = ['name', 'videofile', 'comments', 'lang', 'tags']


@login_required
def new_sequence(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except:
        project = None
    response_data = {}
    if project:
        sequence = VideosSequence(project=project)
        sequence.save()

def get_sequence(request, project):
    try:
        sequence = VideosSequence.objects.filter(project_id=project.id)[0]
    except:
        sequence = ''

    response_data = {}

    if sequence:
        response_data['status'] = 'success'
        response_data['sequence'] = str(sequence.sequence)
    else:
        response_data['status'] = 'failed'
        response_data['sequence'] = ''
    print(response_data)
    return json.dumps(response_data)


def update_sequence(request, project, videos, is_first, is_new):

    response_data = {}
    if not videos:
        videos = []
    if request.method == 'POST':
        sequence = VideosSequence.objects.filter(project_id=project.id)[0]
        if is_new and not is_first:
            sequence.sequence = videos.split(',')
        elif not is_new:
            videos = videos.split(',')
            for i in range(len(request.POST)):
                videos.append(request.POST[i])
            videos = ','.join(videos)
            sequence.sequence = videos
        sequence.save()
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    try:
        sequence = VideosSequence.objects.filter(project_id=project.id)[0]
    except:
        response_data['action'] = 'update_sequence'
        response_data['status'] = 'failed'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    sequence.sequence = str(videos)
    sequence.save()

    response_data['action'] = 'update_sequence'
    response_data['status'] = 'success'
    return json.dumps(response_data)
