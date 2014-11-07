"""
Django settings for moonrain project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z5n&9dh5#lr00x9m-i&ccgx5pkojk0veh4@vw2&jdf1gae$2@v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 'debug_toolbar.apps.DebugToolbarConfig',
    'taggit',
    'suit_redactor',
    'django_jinja',
    'django_extensions',
    'compressor',
    # 'autofixture', # For testing

    'moonrain.videos',
    'moonrain.projects',
    'moonrain.accounts',

    # Comments
    'fluent_comments',
    'crispy_forms',
    'django.contrib.comments',
    #'threadedcomments',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

TEMPLATE_LOADERS = (
    'django_jinja.loaders.AppLoader',
    'django_jinja.loaders.FileSystemLoader',
)

AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/login/'

FLUENT_COMMENTS_EXCLUDE_FIELDS = ('email', 'url')
COMMENTS_APP = 'fluent_comments'

SUIT_CONFIG = {
    'ADMIN_NAME': 'MOONRAIN'
}

ROOT_URLCONF = 'moonrain.urls'

WSGI_APPLICATION = 'moonrain.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',
)


TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)

#Jinja
DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja'
DEFAULT_JINJA2_TEMPLATE_INTERCEPT_RE = r'.*jinja$'  # Не самый хороший вариант

STATIC_ROOT = '/static/'
COMPRESS_ENABLED = True
COMPRESS_PARSER = 'compressor.parser.Html5LibParser'
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
