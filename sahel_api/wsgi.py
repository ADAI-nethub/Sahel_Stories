"""
WSGI config for sahel_api project.

It exposes the WSGI callable as a module-level variable named ``application``.
For more information, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os  # 📁 Importe l'outil pour parler au système d'exploitation (Windows, macOS, etc.)
from pathlib import Path  # 🗺️ Importe l'outil pour trouver des chemins de fichiers et dossiers
from dotenv import load_dotenv  # 🔐 Importe l'outil pour lire le fichier des secrets (.env)
import sys  # 🧠 Importe l'outil pour modifier comment l'ordinateur trouve les programmes

# 🏠 Donne l'adresse du dossier principal de notre projet
path = '/home/yourusername/Sahel_Stories'
# ✅ Vérifie si cette adresse n'est pas déjà dans la liste de recherche de l'ordinateur
if path not in sys.path:
    sys.path.append(path)  # ➕ Ajoute l'adresse à la liste si elle n'y est pas

# 📖 Dit à l'ordinateur : "Le livre de règles de mon site s'appelle sahel_api.settings"
os.environ['DJANGO_SETTINGS_MODULE'] = 'sahel_api.settings'

# 🛠️ Importe l'outil pour construire l'application web
from django.core.wsgi import get_wsgi_application
# 🏗️ Construit l'application et l'appelle "application" pour que le serveur web la trouve
application = get_wsgi_application()

# 🔍 Charge les variables d'environnement depuis le fichier .env à la racine du projet (s'il existe)
# 📂 Trouve le dossier principal du projet en remontant de deux niveaux
BASE_DIR = Path(__file__).resolve().parent.parent
# 🗺️ Crée le chemin complet vers le fichier secret .env
env_path = BASE_DIR / ".env"
# 👀 Vérifie si le fichier .env existe vraiment
if env_path.exists():
    load_dotenv(dotenv_path=env_path)  # 📖 Lit les secrets du fichier .env

# ✅ S'assure que Django connaît le bon fichier de paramètres AVANT de lancer l'application
# 📋 Double vérification : "Pour être sûr, utilise bien le livre de règles sahel_api.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sahel_api.settings")

# 🛠️ Importe à nouveau l'outil pour construire l'application (par sécurité)
from django.core.wsgi import get_wsgi_application  # noqa: E402

# 🏗️ Construit définitivement l'application web finale
application = get_wsgi_application()