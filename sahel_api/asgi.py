"""
Configuration ASGI pour le projet config.

Expose l'application ASGI comme une variable nommée ``application``.

Pour plus d'informations sur ce fichier, voir
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# Fichier : sahel_api/wsgi.py
# Ce fichier est comme la "salle des machines" de ton site web Django.
# Il explique au serveur web (comme Apache ou Gunicorn) comment demarrer Django.

import os  # Pour parler au systeme d'exploitation
from pathlib import Path  # Pour trouver des chemins de dossiers
from dotenv import load_dotenv  # Pour lire les secrets du fichier .env

# On trouve le dossier principal du projet
BASE_DIR = Path(__file__).resolve().parent.parent
# On cree le chemin vers le fichier .env
env_path = BASE_DIR / ".env"

# Si le fichier .env existe, on le lit pour que Django connaisse nos secrets
if env_path.exists():
    load_dotenv(dotenv_path=env_path)

# On dit a Django ou trouver le fichier de parametres (settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sahel_api.settings")

# On demarre l'application WSGI pour que le serveur puisse lancer notre site
from django.core.wsgi import get_wsgi_application  # On importe apres avoir prepare les parametres
application = get_wsgi_application()  # On cree l'application que le serveur utilisera