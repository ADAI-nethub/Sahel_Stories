"""
WSGI config for sahel_api project.

It exposes the WSGI callable as a module-level variable named ``application``.
For more information, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path
from dotenv import load_dotenv  # ✅ correct import

# Load environment variables from the project root .env file (if present)
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

# Ensure Django settings are set before importing WSGI application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sahel_api.settings")

from django.core.wsgi import get_wsgi_application  # noqa: E402

application = get_wsgi_application()
