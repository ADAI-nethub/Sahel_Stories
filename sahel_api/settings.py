# 📘 Django Settings (like the rulebook for your project)
# Made simple, safe, and easy to change with environment variables

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


# 🏠 Find the base folder of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# 📦 Load all secret keys and settings from the .env file
load_dotenv()

# 🛡️ Secret key for Django (like the master password)
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-insecure-key")

# 🕵️ Decide if we are in debug (developer) mode
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# 🌍 Websites allowed to use this server
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# 🍪 For security: which websites can send CSRF cookies
CSRF_TRUSTED_ORIGINS = [
    'https://adai.pythonanywhere.com'
]

# 🚪 Where to go after login/logout
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# 🧩 List of apps we use
INSTALLED_APPS = [
    # 🏗️ Built-in Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🛠️ Extra helpers
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',

    # 📚 Our own apps
    'stories',
    'accounts',
]

# 🚦 Middlemen that check every request
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 📬 Main URL settings
ROOT_URLCONF = "sahel_api.urls"

# 🎨 Templates (HTML pages)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # folder where we keep extra templates
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

# 🚀 Web server starter
WSGI_APPLICATION = "sahel_api.wsgi.application"

# 🗄️ Database (use env variables, default is PythonAnywhere MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'ADAI$sahel_stories'),
        'USER': os.getenv('DB_USER', 'ADAI'),
        'PASSWORD': os.getenv('DB_PASSWORD', ''),  # 🔑 from .env file
        'HOST': os.getenv('DB_HOST', 'ADAI.mysql.pythonanywhere-services.com'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

# 🔐 Password rules
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌎 Language and time
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 🎨 Static files (CSS, JS, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # where Django collects them

# 🎨 Extra static files for development only
if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / "static"]

# 📸 Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 🆔 Default ID type for new models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 📦 REST API settings
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # 🔐 safe by default
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# 🌳 Google Sheets API credentials
# Path to the service account JSON file (can be overridden in .env)
GOOGLE_SHEETS_CREDS = os.getenv(
    "GOOGLE_SHEETS_CREDS",
    str(BASE_DIR / "google-credentials.json")  # fallback if not in .env
)

# Name of the Google Sheet we connect to
GOOGLE_SHEETS_NAME = os.getenv(
    "GOOGLE_SHEETS_NAME",
    "Sahel Tree Planting"  # default sheet name
)
