# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Video
from moonrain.projects.models import Project


def video_list(request):
    all_videos_names = []
    if request.user.has_perm('projects.can_view_project'):
        for video in Video.objects.all():
            all_videos_names.append(video.comments)
    else:
        all_videos_names = '<h1>Access denied</h1>'
    return HttpResponse(str(all_videos_names))


def video_detail(request, id):
    pass