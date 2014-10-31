# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.forms import ModelForm
from django.conf import settings
from django.utils.html import format_html
from suit_redactor.widgets import RedactorWidget
from taggit.managers import TaggableManager


class Project(models.Model):
    name = models.CharField("Название проекта:", max_length=64)
    date = models.DateTimeField("Дата создания:", blank=True, auto_now_add=True, null=True)
    comments = models.TextField("Описание:", blank=True)
    tags = TaggableManager(blank=True)
    is_private = models.BooleanField("Конфиденциальный проект. Доступен только сотрудникам.", default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def Комментарий(self):
        return format_html(self.comments)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'
        permissions = (
            ("can_view_project", "Просмотр проекта"),
            ("can_edit_project", "Редактирование проекта"),
        )


class ProjectForm(ModelForm):
    class Meta:
        widgets = {
            'comments': RedactorWidget(editor_options={'lang': 'ru'})
        }

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('name', 'author', 'date', 'Комментарий')

