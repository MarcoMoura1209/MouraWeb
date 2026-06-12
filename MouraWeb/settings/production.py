from pathlib import Path
from csp.constants import UNSAFE_HASHES
from decouple import Csv, config
from .base import *


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

DEBUG = False

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

RATELIMIT_ENABLE = True

# Cross-site Scripting (XSS)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# SSL redirect
SECURE_SSL_REDIRECT = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#  HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Cross-site request forgery (CSRF) protection
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CONTENT_SECURITY_POLICY = {
    'DIRECTIVES': {
        'default-src': ("'self'",),
        'script-src': (
            "'self'",
            "https://code.iconify.design",
            "https://cdnjs.cloudflare.com",
        ),
        'style-src': (
            "'self'",
            UNSAFE_HASHES,
            "'sha256-l+LQCZo1PCpc6+cP1IqeAjOu62qLmYkCdGNc9KErS/o='",
            "https://cdnjs.cloudflare.com",
            "https://fonts.googleapis.com",
        ),
        'font-src': (
            "'self'",
            "https://fonts.gstatic.com",
            "https://cdnjs.cloudflare.com",
        ),
        'img-src': ("'self'",),
    }
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET'),
}

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
