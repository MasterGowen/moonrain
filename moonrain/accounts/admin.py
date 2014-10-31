# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ('email', 'username', 'first_name', 'last_name', 'is_admin',)
    list_filter = ('is_admin',) 
    fieldsets = (
        (None, {'fields': ('email', 'username')}),
        ('Персональная информация', {'fields': (('first_name', 'last_name'), 'department', 'avatar')}),
        ('Проекты и права', {'fields': ('is_admin', 'projects')}),
        ('Даты', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)