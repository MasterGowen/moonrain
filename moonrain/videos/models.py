from django.db import models
from django.conf import settings
from django.utils.html import format_html
from durationfield.db.models.fields.duration import DurationField
from taggit.managers import TaggableManager
from moonrain.projects.models import Project
import os
import uuid
from os import urandom
import hashlib
import time


def key():

    key = hashlib.md5(urandom(128)).hexdigest()
    return key


def generate_new_filename(instance, filename):
    f, ext = os.path.splitext(filename)
    filename = '%s%s' % (uuid.uuid4().hex, ext)
    fullpath = time.strftime('%Y/%m') + '/' + key() + '/' + filename
    return fullpath



class Video(models.Model):
    '''
    Видео
    '''

    parent = models.IntegerField("ID родителя", null=True, default=None)

    videofile = models.FileField("Видеофайл:", null=True, default=None, upload_to=generate_new_filename)

    #VIDEO
    name = models.CharField("Название видео:", max_length=64)
    url = models.URLField("Ссылка:", max_length=256, blank=True, null=True)
    date = models.DateTimeField("Дата загрузки:", blank=True, auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    project = models.ForeignKey(Project, null=True)
    resolution = models.CharField("Разрешение:", max_length=12, blank=True)
    vcodec = models.CharField("Видеокодек:", max_length=32, blank=True)
    aspect = models.CharField("Соотношение сторон:", max_length=8, blank=True)
    vbitrate = models.CharField("Битрейт видео:", max_length=16, blank=True)
    duration = DurationField("Продолжительность:", blank=True, null=True)
    lang = models.CharField("Язык видео:", max_length=32, blank=True)

    #AUDIO
    audio = models.BooleanField("Наличие аудио:", default=True)
    acodec = models.CharField("Аудиокодек:", max_length=32, blank=True)
    abitrate = models.CharField("Битрейт аудио:", max_length=16, blank=True)
    CHANNELS_CHOISES = (
        ("1", "MONO"),
        ("2", "STEREO"),
    )
    channels = models.CharField("Каналы:", max_length=1, choices=CHANNELS_CHOISES, blank=True)

    comments = models.TextField("Описание:", blank=True)
    tags = TaggableManager(blank=True)
    encoded = models.BooleanField("Перекодирован:", default=False)
    def Комментарий(self):
        return format_html(self.comments)

    class Meta:
        verbose_name = ('видео')
        verbose_name_plural = ('видео')

    def get_absolute_url(self):
        return "/videos/%i/" % self.id
