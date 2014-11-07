from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Video


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


def video_detail(request, video_id):
    pass