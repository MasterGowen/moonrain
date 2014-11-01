moonrain for UrFU
=================


Django проект, реализующий хостинг видеофайлов, разнесённых по проектам.


Requirements:
=============

    python==3.4.1
    Django==1.7.1 (likely 1.8)
    django-taggit==0.12.2
    django-durationfield==0.5.1
    django-suit==0.2.11
    django-suit-redactor==0.0.2
    django-suit-locale==1.0.9
    django-debug-toolbar==1.2.2
    django-authtools==1.0.0
    South==1.0.1
    Pillow==2.6.1

Установка
=========
    pip install -r requirements.txt
    manage.py makemigrations
    manage.py migrate
    manage.py createsuperuser
    manage.py runserver

