from pathlib import Path
import os
import dj_database_url




# 👇 Redirect after login/logout
LOGIN_REDIRECT_URL = "/"      # after login, go to home
LOGOUT_REDIRECT_URL = "/"     # after logout, go to home


BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_URLCONF = "sahel_api.urls"

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': 
        'django_filters.rest_framework.DjangoFilterBackend',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# Core settings
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-dev-key-only')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

DATABASE_URL = os.getenv('DATABASE_URL')

# Database config
if DATABASE_URL and DATABASE_URL.startswith('postgres'):
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            ssl_require=not DEBUG  # Only require SSL in production
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
        
    # your apps
    'rest_framework',  # Django REST Framework
    'stories',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',   # ✅ required
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # ✅ required
    'django.contrib.messages.middleware.MessageMiddleware',     # ✅ required
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

BASE_DIR = Path(__file__).resolve().parent.parent
        # 👇 Add templates folder
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # <--- important!
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

# 👇 Redirect after login/logout
LOGIN_REDIRECT_URL = "/"      # after login, go to home
LOGOUT_REDIRECT_URL = "/"     # after logout, go to home

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# (Optional, but recommended during development)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# (Optional, for production when you collect static files)
STATIC_ROOT = BASE_DIR / "staticfiles"
