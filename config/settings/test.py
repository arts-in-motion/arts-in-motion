from .base import *

# BASE_NAME and BASE_DOMAIN are intentionally unset
# None of the commands that rely on these values should run during tests
BASE_URL = "http://example.com"

###############################################################################
# Core

TEST = True
DEBUG = True
SECRET_KEY = 'test'

LOGGING['loggers']['portal']['level'] = 'DEBUG'

###############################################################################
# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'artsinmotion_test',
        'HOST': '127.0.0.1',
    }
}
