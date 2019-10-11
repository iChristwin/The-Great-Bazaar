# Inherit from standard settings file for defaults
# Everything below will override our standard settings:
# Parse database configuration from $DATABASE_URL

import dj_database_url
import django_heroku

from .base import *


DATABASES['default'] = dj_database_url.config()

DOMAIN = 'https://the-great-bazaar.herokuapp.com'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # I added whitenoise here
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow specific host headers
ALLOWED_HOSTS = ['the-great-bazaar.herokuapp.com',
                 '127.0.0.1', "localhost",
                 "0.0.0.0", ".herokuapp.com",
                 ]

# Set debug to False
DEBUG = False

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


django_heroku.settings(locals())
