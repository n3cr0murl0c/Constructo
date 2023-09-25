from .base import *
import sys

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "constructo_db",
        "USER": "postgres",
        "PASSWORD":"ch@nge_me_pls",
        "HOST": "db.host.changeme.pls",
        "PORT":  "5432",
    },
    
}
if 'test' in sys.argv or 'test_coverage' in sys.argv: #Covers regular testing and django-coverage
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
SECRET_KEY = 'django-insecure-b28ctt5p*m_esix@gkzj4k+i^u_ozbu)9eoyn#e-rv8c(a8=$f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

