from django.db import models
from django.conf import settings
from django.utils.html import format_html
from taggit.managers import TaggableManager


class Project(models.Model):
    """
    Проект
    """
    name = models.CharField("Название проекта:", max_length=64)
    date = models.DateTimeField("Дата создания:", blank=True, auto_now_add=True, null=True)
    comments = models.TextField("Описание:", blank=True)
    tags = TaggableManager(blank=True)

    VISIBLITY_STATUS = (
        ('public', 'Опубликован'),
        ('for_users', 'Доступен сотрудникам'),
        ('for_staff', 'Не опубликован')
    )
    permission = models.CharField('Права доступа:', max_length=255, choices=VISIBLITY_STATUS)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def users(self):
        users = []
        for user in self.user_set.all():
            users.append(user.username + ': ' + user.email)
        return format_html('<br />'.join(users))

    def Комментарий(self):
        return format_html(self.comments)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/project/%i/" % self.id

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'
        permissions = (
            ("can_view_project", "Просмотр проекта"),
            ("can_edit_project", "Редактирование проекта"),
        )
