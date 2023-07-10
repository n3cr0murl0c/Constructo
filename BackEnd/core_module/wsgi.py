"""
WSGI config for IDS_APP project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
from whitenoise import WhiteNoise
from django.conf import settings
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Icore_module.settings.production")

application = WhiteNoise(get_wsgi_application(), root=settings.STATIC_ROOT)
