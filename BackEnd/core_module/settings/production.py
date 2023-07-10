

from .base import *
import sys

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "constructo_db",
        "USER": "postgres",
        "PASSWORD":"@nDREE1%",
        "HOST": "msp_db.v3ntrue.xyz",
        "PORT":  "5432",
    },
    
}
if 'test' in sys.argv or 'test_coverage' in sys.argv: #Covers regular testing and django-coverage
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
SECRET_KEY = '7@3r)xo@*a_v+tyn7i5y8a27x8v23v8igkx9@x=86jd93838m7'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' :[
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',

    ]
}
DEBUG = False

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "localhost", "idf.v3ntrue.xyz", ]

CSRF_TRUSTED_ORIGINS = ["https://*.v3ntrue.xyz"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
SECURE_HSTS_SECONDS = 2,592,000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True