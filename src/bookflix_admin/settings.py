"""
Django settings for bookflix_admin project.

Generated by 'django-admin startproject' using Django 3.2.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_APP_SECRET_KEY', default='change-me')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', default=1)))

ALLOWED_HOSTS = []
ALLOWED_HOSTS_ENV = os.environ.get('ALLOWED_HOSTS')
if ALLOWED_HOSTS_ENV:
    ALLOWED_HOSTS.extend(ALLOWED_HOSTS_ENV.split(','))

if DEBUG:
    ALLOWED_HOSTS.extend('*')

# Application definition

INSTALLED_APPS = [
    'core',
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'baton.autodiscover'
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookflix_admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookflix_admin.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if DEBUG and not os.environ.get("AWS_RDS_POSTGRES_HOST_URL"):
    # print('sqlite', os.environ.get('AWS_RDS_POSTGRES_DB_NAME'))
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    # print('postgres', os.environ.get('AWS_RDS_POSTGRES_DB_NAME'))
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('AWS_RDS_POSTGRES_DB_NAME'),
            'USER': os.environ.get('AWS_RDS_POSTGRES_MASTER_USERNAME'),
            'PASSWORD': os.environ.get('AWS_RDS_POSTGRES_MASTER_PASSWORD'),
            'HOST': os.environ.get('AWS_RDS_POSTGRES_HOST_URL'),
            'PORT': 5432
        }
    }

BATON = {
    'SITE_HEADER': 'BOOKFLIX',
    'SITE_TITLE': 'BOOKFLIX',
    'INDEX_TITLE': 'BOOKFLIX ADMIN',
    'SUPPORT_HREF': 'https://github.com/ashiqursuperfly/bookflix-admin/issues',
    'COPYRIGHT': 'copyright © 2020 <a href="https://github.com/ashiqursuperfly/bookflix-admin/">BOOKFLIX</a>',
    'POWERED_BY': '<a href="https://github.com/ashiqursuperfly/bookflix-admin/">BOOKFLIX</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU_TITLE': 'Menu',
    'MESSAGES_TOASTS': False,
    'GRAVATAR_DEFAULT_IMG': 'identicon',
    'LOGIN_SPLASH': '/static/core/img/book.png',
    # 'SEARCH_FIELD': {
    #     'label': 'Search contents...',
    #     'url': '/search/',
    # },
    'MENU': (
        {'type': 'title', 'label': 'main', 'apps': ('auth',)},
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },
        {'type': 'title', 'label': 'Manage', 'apps': ('core',)},
        {
            'type': 'app',
            'name': 'core',
            'label': 'Core',
            'icon': 'fas fa-book-open',
            'models': (
                {
                    'name': 'reader',
                    'label': 'Readers'
                },
                {
                    'name': 'author',
                    'label': 'Authors'
                },
                {
                    'name': 'genre',
                    'label': 'Genres'
                },
                {
                    'name': 'book',
                    'label': 'Books'
                },
            )
        },
        # { 'type': 'title', 'label': 'Contents', 'apps': ('flatpages', ) },
        # { 'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages' },
        # { 'type': 'free', 'label': 'Custom Link', 'url': 'http://www.google.it', 'perms': ('flatpages.add_flatpage', 'auth.change_user') },
        # { 'type': 'free', 'label': 'My parent voice', 'default_open': True, 'children': [
        #     { 'type': 'model', 'label': 'A Model', 'name': 'mymodelname', 'app': 'myapp' },
        #     { 'type': 'free', 'label': 'Another custom link', 'url': 'http://www.google.it' },
        # ] },
    )
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# TODO: for deployment
# STATIC_URL = '/static/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
# MEDIA_URL = '/static/media/'
# MEDIA_ROOT = '/vol/web/media'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
# AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_CLOUDFRONT_DOMAIN')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_ADDRESSING_STYLE = "virtual"

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
