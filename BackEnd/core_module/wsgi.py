from whitenoise import WhiteNoise
from django.conf import settings
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core_module.settings.production")

application = WhiteNoise(get_wsgi_application(), root=settings.STATIC_ROOT)
