"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

#  sahel_api/wsgi.py
# This file is like the "engine room" ⚙️ of your Django website.
# It tells the web server (like Apache or Gunicorn) how to start Django.

import os
from pathlib import Path
from dotenv import load_dotenv  # 🪄 lets us read secret stuff from the .env file

# Find the .env file in the project’s main folder
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"

# If the .env file exists, read it so Django knows our secrets
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

# Tell Django where to find the settings file
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sahel_api.settings")

# Start the WSGI application so the server can run our site
from django.core.wsgi import get_wsgi_application  # we import this only after settings are ready
application = get_wsgi_application()

