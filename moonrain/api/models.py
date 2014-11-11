from django.db import models
from django.contrib import admin
from os import urandom
from base64 import b64encode


def randstring():

    key = b64encode(urandom(32)).decode('utf-8')
    return key[:31]


class Server(models.Model):

    name = models.CharField('Название:', max_length=255)
    api_key = models.CharField('Ключ:', max_length=32, unique=True, default=randstring())


class ServerAdmin(admin.ModelAdmin):

    list_display = ('name', 'api_key')
    readonly_fields = ('api_key',)

admin.site.register(Server, ServerAdmin)