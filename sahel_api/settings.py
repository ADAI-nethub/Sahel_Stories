"""
Sahel_Stories Django Settings

This file controls how the website works behind the scenes.
It sets up the database, security, apps, and other key features.
Never commit secrets (like SECRET_KEY) to GitHub.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url


# 🏠 BASE_DIR: Finds the main folder of your project
# Think: "Where is this file located? Go two folders up — that's the project root!"
# "This helps the computer find your project, like a treasure map!"
BASE_DIR = Path(__file__).resolve().parent.parent


# 🔍 load_dotenv(): Loads secrets from a .env file (if you're using one)
# "It's like whispering passwords so no one else can see them."
# But on Render, we use Environment Variables instead — safer!
load_dotenv()


# 🛡️ SECRET_KEY: Super-secret password for your website
#  "This is like a magic key that keeps hackers out!"
# 🔐 Crash if not set — good for production (no weak defaults!)
SECRET_KEY = os.environ["SECRET_KEY"]


# 🕵️ DEBUG: Turns on error messages (good for fixing bugs)
# "If something breaks, should the website tell you how? Only during testing!"
# ⚠️ Never use DEBUG = True in production!
DEBUG = os.getenv("DEBUG", "False").lower() == "true"


# 🌍 ALLOWED_HOSTS: Which websites can visit your app
#  "Only these addresses are allowed in. Like a guest list for a party!"
ALLOWED_HOSTS = [
    'sahel-stories-1.onrender.com',  # Your live website
    'localhost',                     # Your computer (for testing)
    '127.0.0.1'                      # Another way to say 'your computer'
]


# 🍪 CSRF_TRUSTED_ORIGINS: Safe websites that can send data to your site
# "If a form comes from this address, it's trusted — like a secret handshake."
# ❌ Fix: Remove trailing space in the URL!
CSRF_TRUSTED_ORIGINS = [
    'https://sahel-stories-1.onrender.com'  # No space at the end!
]


# 🚪 LOGIN/LOGOUT Redirects: Where to go after login/logout
# "After you log in, go to the homepage. Same after logging out."
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


# 🧩 INSTALLED_APPS: All the tools (apps) your website uses
# "These are like LEGO pieces — each one adds a new feature!"
INSTALLED_APPS = [
    # Django's built-in tools
    'django.contrib.admin',            # Admin panel (like a control center)
    'django.contrib.auth',             # Login/logout system
    'django.contrib.contenttypes',     # Helps Django understand data types
    'django.contrib.sessions',         # Remembers who's logged in
    'django.contrib.messages',         # Shows temporary messages ("Saved!")
    'django.contrib.staticfiles',      # Serves CSS, JS, images

    # Extra tools we added
    'django_filters',                  # Lets users filter stories
    'rest_framework',                  # For building an API
    'rest_framework.authtoken',        # For API login with tokens

    # Our own apps
    'stories',                         # Handles stories and tree planting
    'accounts',                        # Handles user accounts
]

# settings.py
LANGUAGES = [
    ('en', 'English'),
    ('fr', 'Français'),
    ('ar', 'العربية'),
]


# 🚦 MIDDLEWARE: Security guards that check every visitor
# "Like bouncers at a club — they check IDs, stop bad requests, etc."
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',           # Adds security headers
    'django.contrib.sessions.middleware.SessionMiddleware',    # Tracks logged-in users
    'django.middleware.common.CommonMiddleware',               # Handles common web rules
    'django.middleware.csrf.CsrfViewMiddleware',               # Stops fake form attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Checks login status
    'django.contrib.messages.middleware.MessageMiddleware',    # Enables messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Stops clickjacking
    'whitenoise.middleware.WhiteNoiseMiddleware',              # Serves static files fast
    'django.middleware.locale.LocaleMiddleware', 
]


# 📦 STATICFILES_STORAGE: How to store CSS, JS, images
#  "This makes your website load faster by compressing files."
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Where static files live
STATIC_URL = '/static/'           # Web URL: /static/style.css
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Folder where collectstatic puts files

# During development, also look here:
if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / "static"]  # Local static files


# 🎨 TEMPLATES: Where to find HTML files
# "These are the pages your website shows — like story cards or forms."
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Look in /templates/ folder
        'APP_DIRS': True,                  # Also look inside each app
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


# 🚀 WSGI_APPLICATION: Entry point for the web server
# "This tells the web server where to start — like the front door!"
WSGI_APPLICATION = "sahel_api.wsgi.application"


# 🗄️ DATABASES: Where your data is stored
# "This is your website's memory — where stories and trees are saved."
# Uses DATABASE_URL from Render (PostgreSQL)
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}


# 🔐 AUTH_PASSWORD_VALIDATORS: Rules to keep passwords strong
# "Don't let people use '123456' as a password!"
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# 🌎 LANGUAGE & TIME ZONE
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True   # Supports multiple languages (future)
USE_TZ = True     # Uses time zones (recommended)


# 📸 MEDIA FILES: Uploads like photos (only for dev)
#"Where uploaded photos go — but only on  computer!"
# ⚠️ In production, use AWS S3 or Cloudinary!
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# 🆔 DEFAULT_AUTO_FIELD: Default type for new database IDs
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 📦 REST_FRAMEWORK: Settings for the API
# "Rules for how the API works — who can use it and how."
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Only logged-in users
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}


# 🌳 GOOGLE SHEETS (Optional)
#"If you want to save tree plantings to a Google Sheet, set this up!"
# Disabled for now — can be added later with environment variables
# GOOGLE_SHEETS_NAME = os.getenv("GOOGLE_SHEETS_NAME", "Sahel Tree Planting")