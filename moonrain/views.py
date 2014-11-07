from django.shortcuts import render_to_response


def moon_404(request):
    return render_to_response('404.html')


def moon_403(request):
    return render_to_response('403.html')


def moon_500(request):
    return render_to_response('500.html')