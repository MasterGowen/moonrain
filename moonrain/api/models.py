from django.db import models
from django.contrib import admin
from os import urandom
import hashlib


def api_key():

    key = hashlib.md5(urandom(128)).hexdigest()
    return key


class Encoder(models.Model):

    name = models.CharField('Название:', max_length=255)
    description = models.TextField('Описание:', null=True, blank=True)
    api_key = models.CharField('Ключ:', max_length=32, unique=True, default=api_key)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'кодировщик'
        verbose_name_plural = 'кодировщики'


class Client(models.Model):

    name = models.CharField('Название:', max_length=255)
    description = models.TextField('Описание:', null=True, blank=True)
    api_key = models.CharField('Ключ:', max_length=32, unique=True, default=api_key)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class EncoderAdmin(admin.ModelAdmin):

    list_display = ('name', 'api_key', 'description')
    readonly_fields = ('api_key',)


class ClientAdmin(admin.ModelAdmin):

    list_display = ('name', 'api_key', 'description')
    readonly_fields = ('api_key',)


admin.site.register(Encoder, EncoderAdmin)
admin.site.register(Client, ClientAdmin)