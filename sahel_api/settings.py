from pathlib import Path
import os
import dj_database_url
import django
django.setup()  # This will configure Django settings
# Add at the top of settings.py
import os
from dotenv import load_dotenv

# Debug
DEBUG = False  # Must be False on live site

# Allowed Hosts
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

# Static Files
STATIC_ROOT = '/home/yourusername/sahel_api/static'
STATIC_URL = '/static/'

# Database (PythonAnywhere uses SQLite by default)
# Keep default unless you want to upgrade


load_dotenv()  # Load environment variables

# Use environment variables
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

ALLOWED_HOSTS = ['ADAI.pythonanywhere.com']


ALLOWED_HOSTS = ['*']

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


# Use MySQL instead of SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ADAI$default',           # Database name
        'USER': 'ADAI',                   # Your username
        'PASSWORD': 'your_mysql_password', # Set this in next step
        'HOST': 'ADAI.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
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
    'rest_framework.authtoken',
    'django.contrib.staticfiles', 
    
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
