# Inherit from standard settings file for defaults
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']
DOMAIN = 'https://the-great-bazaar.herokuapp.com'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
