"""
Fichier de configuration principal de Django pour le projet Sahel_Stories.
Ce fichier contient toutes les règles et paramètres nécessaires au bon fonctionnement du site web.
Il utilise des variables d'environnement pour garder les informations sensibles (comme les mots de passe) en sécurité.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# 🏠 Définit le chemin du dossier principal du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔍 Charge les variables d'environnement depuis le fichier .env
load_dotenv()

# 🛡️ Clé secrète — DO NOT COMMIT .env OR JSON FILES
SECRET_KEY = os.environ["SECRET_KEY"]  # Will crash if not set — good for production

# 🕵️ Mode débogage
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# 🌍 Allowed hosts — must match your Render URL
ALLOWED_HOSTS = [
    'sahel-stories-1.onrender.com',
    'localhost',
    '127.0.0.1'
]

# 🍪 CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'https://sahel-stories-1.onrender.com'
]

# 🚪 Redirections
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# 🧩 Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',

    'stories',
    'accounts',
]

# 🚦 Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / "static"]

# Templates
ROOT_URLCONF = "sahel_api.urls"
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

# WSGI
WSGI_APPLICATION = "sahel_api.wsgi.application"

# 🗄️ Database
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# 🔐 Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌎 Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 📸 Media files (only for dev; use S3 in prod)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 🆔 Auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 📦 REST Framework
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# 🌳 Google Sheets (optional — only if needed)
# GOOGLE_SHEETS_NAME = os.getenv("GOOGLE_SHEETS_NAME", "Sahel Tree Planting")