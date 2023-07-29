
from os import environ, path
from pathlib import Path
from django.urls import reverse_lazy
from django.contrib import messages


BASE_DIR = Path(__file__).resolve().parent.parent

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Usuarios',
    'blog',
    'blog_api',
    'rest_framework',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",#SIEMPRE DEBE IR DESPUES DE SECURITY MCED
    "corsheaders.middleware.CorsMiddleware",#Debe ir arriba del CommonMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core_module.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core_module.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-es'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
TEMPLATE_PATH = path.join(Path(__file__).resolve().parent.parent.parent, "Templates")
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            TEMPLATE_PATH,
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_DIRS = [
    path.join(Path(__file__).resolve().parent.parent.parent, "static"),
    # Path(__file__).resolve().parent.parent.parent / "static"
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
# web accessible folder
#STATIC_ROOT = '/home/your_name/www/mealmate/static/'
STATIC_ROOT = Path(__file__).resolve().parent.parent.parent / "staticfiles"
# print(f"STATIC SIRVIENDO AQUI ---------->>>>>>>{STATIC_ROOT}<<<<<<<<<<-----------")
STATIC_URL = "static/"
# MEDIA_ROOT ='/usr/src/media/'
MEDIA_ROOT = Path(__file__).resolve().parent.parent.parent / "media"
MEDIA_URL = "media/"
# print(path.join(Path(__file__).resolve().parent.parent,'static'))
# print(STATIC_ROOT,MEDIA_ROOT)

SECURE_HSTS_SECONDS = 2_592_000
LOGIN_URL = reverse_lazy("login")
LOGIN_REDIRECT_URL = reverse_lazy("Inicio")

AUTH_USER_MODEL = "Usuarios.User"


# BOOTSTRAP'S TOAST PANELS
MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}


DATE_INPUT_FORMATS = ['%d/%m/%Y']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    # "http://*.v3ntrue.xyz",
    # "http://127.0.0.1:8000/",
]