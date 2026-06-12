import copy
import os
from .base import *


DEBUG = True
ALLOWED_HOSTS = ['*']
RATELIMIT_ENABLE = False

# SSL redirect
SECURE_SSL_REDIRECT = False


LOGGING = copy.deepcopy(LOGGING)

LOGGING['handlers']['file'] = {
    'level': 'DEBUG',
    'class': 'logging.handlers.RotatingFileHandler',
    'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),
    'maxBytes': 1024 * 1024 * 5,  # 5MB
    'backupCount': 3,
    'formatter': 'simple',
}

LOGGING['loggers']['django']['handlers'] = ['console', 'file']
LOGGING['loggers']['django']['level'] = 'DEBUG'

LOGGING['loggers']['core']['handlers'] = ['console', 'file']
LOGGING['loggers']['core']['level'] = 'DEBUG'

LOGGING['loggers']['django.db.backends'] = {
    'level': 'DEBUG',
    'handlers': ['console'],
    'propagate': False,
}
