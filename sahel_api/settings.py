from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

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
