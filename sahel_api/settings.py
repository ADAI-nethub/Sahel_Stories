# 📘 Django Settings (comme le livre de règles de ton projet)
# Rendu simple, sécurisé et facile à changer avec des variables d'environnement

import os  # 📁 Outil pour parler au système d'exploitation
from pathlib import Path  # 🗺️ Outil pour trouver des chemins de dossiers
from dotenv import load_dotenv  # 🔍 Outil pour lire les secrets


ALLOWED_HOSTS = [
    'ADAI.pythonanywhere.com',
    'localhost',
    '127.0.0.1'
]

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = '/home/ADAI/Sahel_Stories/staticfiles'  # Collected static files
STATICFILES_DIRS = [
    '/home/ADAI/Sahel_Stories/static',
]



# 🏠 Trouve le dossier principal du projet (2 niveaux au-dessus de ce fichier)
BASE_DIR = Path(__file__).resolve().parent.parent

# 📦 Charge tous les secrets et paramètres depuis le fichier .env
load_dotenv()

# 🛡️ Clé secrète pour Django (comme le mot de passe maître)
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-insecure-key")

# 🕵️ Décide si on est en mode debug (mode développeur)
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# 🌍 Sites web autorisés à utiliser ce serveur
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# 🍪 Pour la sécurité : quels sites web peuvent envoyer des cookies CSRF
CSRF_TRUSTED_ORIGINS = [
    'https://adai.pythonanywhere.com'
]

# 🚪 Où aller après connexion/déconnexion
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# 🧩 Liste des applications que nous utilisons
INSTALLED_APPS = [
    # 🏗️ Applications intégrées à Django
    'django.contrib.admin',          # 👨‍💼 Panneau d'administration
    'django.contrib.auth',           # 🔐 Gestion des utilisateurs
    'django.contrib.contenttypes',   # 📦 Types de contenu
    'django.contrib.sessions',       # 💺 Gestion des sessions
    'django.contrib.messages',       # 💬 Système de messages
    'django.contrib.staticfiles',    # 🎨 Fichiers statiques (CSS, JS)

    # 🛠️ Aides supplémentaires
    'django_filters',                # 🔍 Filtres pour les données
    'rest_framework',                # 📡 Framework pour API REST
    'rest_framework.authtoken',      # 🔑 Tokens d'authentification

    # 📚 Nos propres applications
    'stories',                       # 📖 Application des histoires
    'accounts',                      # 👤 Application des comptes
]

# 🚦 Intermédiaires qui vérifient chaque requête
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',          # 🛡️ Sécurité
    'django.contrib.sessions.middleware.SessionMiddleware',   # 💺 Sessions
    'django.middleware.common.CommonMiddleware',              # 🌍 Common
    'django.middleware.csrf.CsrfViewMiddleware',              # 🍪 Protection CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # 🔐 Authentification
    'django.contrib.messages.middleware.MessageMiddleware',   # 💬 Messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # 🚫 Anti-clickjacking
]

# 📬 Paramètres principaux des URLs
ROOT_URLCONF = "sahel_api.urls"

# 🎨 Templates (pages HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # 📁 Dossier où on garde les templates supplémentaires
        'APP_DIRS': True,  # ✅ Cherche aussi les templates dans chaque application
        'OPTIONS': {
            'context_processors': [  # 🎭 Processeurs qui ajoutent des infos aux templates
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🚀 Lanceur du serveur web
WSGI_APPLICATION = "sahel_api.wsgi.application"

# 🗄️ Base de données (utilise SQLite par défaut pour la simplicité)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # 🗃️ Type de base de données
        'NAME': BASE_DIR / 'db.sqlite3',         # 📊 Fichier de la base de données
    }
}

# 🔐 Règles pour les mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # ❌ Pas trop similaire au nom
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},            # 📏 Longueur minimum
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},           # 🚫 Pas un mot de passe commun
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},          # 🔢 Pas que des chiffres
]

# 🌎 Langue et fuseau horaire
LANGUAGE_CODE = 'en-us'  # 🇺🇸 Langue anglaise
TIME_ZONE = 'UTC'        # 🌐 Fuseau horaire universel
USE_I18N = True          # ✅ Active l'internationalisation
USE_TZ = True            # ✅ Utilise les fuseaux horaires

# 🎨 Fichiers statiques (CSS, JS, Images)
STATIC_URL = '/static/'  # 🌐 URL pour accéder aux fichiers statiques
STATIC_ROOT = BASE_DIR / 'staticfiles'  # 📦 Où Django collecte tous les fichiers statiques

# 🎨 Fichiers statiques supplémentaires pour le développement seulement
if DEBUG:  # 🛠️ Seulement en mode développement
    STATICFILES_DIRS = [BASE_DIR / "static"]

# 📸 Fichiers média (uploads)
MEDIA_URL = '/media/'  # 🌐 URL pour accéder aux fichiers uploadés
MEDIA_ROOT = BASE_DIR / 'media'  # 📁 Dossier où sont stockés les fichiers uploadés

# 🆔 Type d'ID par défaut pour les nouveaux modèles
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 📦 Paramètres de l'API REST
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],  # 🔍 Filtres
    'DEFAULT_AUTHENTICATION_CLASSES': [  # 🔐 Méthodes d'authentification
        'rest_framework.authentication.SessionAuthentication',  # 💺 Sessions
        'rest_framework.authentication.TokenAuthentication',    # 🔑 Tokens
    ],
    'DEFAULT_PERMISSION_CLASSES': [  # 🚫 Permissions par défaut
        'rest_framework.permissions.IsAuthenticated',  # 🔐 Sécurité par défaut
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # 📄 Pagination
    'PAGE_SIZE': 10  # 🔢 10 éléments par page
}

# 🌳 Identifiants de l'API Google Sheets
# Chemin vers le fichier JSON du compte de service (peut être changé dans .env)
GOOGLE_SHEETS_CREDS = os.getenv(
    "GOOGLE_SHEETS_CREDS",
    str(BASE_DIR / "google-credentials.json")  # 📁 Fichier par défaut si pas dans .env
)

# Nom du Google Sheet auquel on se connecte
GOOGLE_SHEETS_NAME = os.getenv(
    "GOOGLE_SHEETS_NAME",
    "Sahel Tree Planting"  # 🌳 Nom par défaut de la feuille
)