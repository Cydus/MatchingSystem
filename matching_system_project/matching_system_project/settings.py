# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os

DJANGO_SETTINGS_MODULE = 'settings'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Project path
PROJECT_PATH = os.path.join(BASE_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)

# Template path
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')

# Static Path
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i84^!30#_tk$^xqhx#1o#hs(k23rf*)#u8erdj(n&sb^+qa$&('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

ADMINS = (
    ('Webmaster', 'webmaster@pro')
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'matching_system_project.urls'

WSGI_APPLICATION = 'matching_system_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Installed Applications
# http://www.tangowithdjango.com/book/chapters/setup.html

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'matching_system_project'
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    STATIC_PATH,
)

# Templates Directory
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)

# Media Director
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH,
                          'matching_system_project/matching_system_project/media')  # Absolute path to the media directory

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'vaspetr506@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'vaspetr506@gmail.com'
EMAIL_HOST_PASSWORD = 'Django2014'
EMAIL_PORT = 587
SERVER_EMAIL = 'vaspetr506@gmail.com'


