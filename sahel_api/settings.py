<<<<<<< HEAD
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
=======
"""
Fichier de configuration principal de Django pour le projet Sahel_Stories.
Ce fichier contient toutes les règles et paramètres nécessaires au bon fonctionnement du site web.
Il utilise des variables d'environnement pour garder les informations sensibles (comme les mots de passe) en sécurité.
"""

import os  # Module pour interagir avec le système d'exploitation (lire des fichiers, des dossiers, etc.)
from pathlib import Path  # Outil pour gérer les chemins de fichiers de manière sûre, sur tous les systèmes
from dotenv import load_dotenv  # Permet de charger les variables d'environnement depuis un fichier .env

# 🏠 Définit le chemin du dossier principal du projet (deux niveaux au-dessus de ce fichier settings.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔍 Charge les variables d'environnement depuis le fichier .env (utile pour garder les secrets)
load_dotenv()

# 🛡️ Clé secrète de Django – très importante pour la sécurité (comme un mot de passe maître)
# Elle est lue depuis le fichier .env. Si elle n'existe pas, une valeur par défaut est utilisée (moins sécurisée)
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-insecure-key")

# 🕵️ Mode débogage : affiche les erreurs en détail si True, cache les erreurs si False
# Utile pendant le développement, mais dangereux en production
# La valeur vient du fichier .env, convertie en booléen
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# 🌍 Liste des noms de domaine ou adresses IP autorisés à accéder à ce site
# Par exemple : "localhost" pour le test en local, ou "monsite.com" en production
# Lu depuis le fichier .env, séparé par des virgules
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# 🍪 Liste des origines de confiance pour les requêtes CSRF (protection contre les attaques)
# Important si vous utilisez des formulaires ou une API
CSRF_TRUSTED_ORIGINS = [
    'https://adai.pythonanywhere.com'  # Site autorisé à envoyer des données sécurisées
]

# 🚪 Redirection après connexion ou déconnexion
LOGIN_REDIRECT_URL = "/"      # Aller à la page d'accueil après s'être connecté
LOGOUT_REDIRECT_URL = "/"     # Aller à la page d'accueil après s'être déconnecté

# 🧩 Applications installées dans le projet
# Chaque application ajoute des fonctionnalités spécifiques
INSTALLED_APPS = [
    # Applications Django de base
    'django.contrib.admin',            # Interface d'administration (panneau de contrôle)
    'django.contrib.auth',             # Gestion des comptes utilisateurs
    'django.contrib.contenttypes',     # Système interne pour gérer les types de contenu
    'django.contrib.sessions',         # Mémorise qui est connecté (session utilisateur)
    'django.contrib.messages',         # Affiche des messages temporaires (ex: "Enregistré avec succès")
    'django.contrib.staticfiles',      # Gère les fichiers statiques (CSS, JS, images)

    # Applications tierces utiles
    'django_filters',                  # Permet de filtrer les données (ex: trier des histoires)
    'rest_framework',                  # Pour créer une API (échange de données)
    'rest_framework.authtoken',        # Permet d'utiliser des jetons d'accès (tokens)

    # Nos propres applications
    'stories',                         # Application qui gère les histoires
    'accounts',                        # Application qui gère les comptes utilisateurs
]

# 🚦 Middleware : outils qui vérifient chaque requête entrante
# Ils assurent la sécurité, la session, la protection, etc.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',           # Sécurité (protections automatiques)
    'django.contrib.sessions.middleware.SessionMiddleware',    # Gère la session utilisateur
    'django.middleware.common.CommonMiddleware',               # Gère les requêtes courantes
    'django.middleware.csrf.CsrfViewMiddleware',               # Protège contre les attaques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Vérifie si l'utilisateur est connecté
    'django.contrib.messages.middleware.MessageMiddleware',    # Active les messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Empêche l'intégration malveillante
]

# 📬 Fichier principal qui gère toutes les adresses du site (URLs)
ROOT_URLCONF = "sahel_api.urls"

# 🎨 Configuration des templates (pages HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Moteur de templates Django
        'DIRS': [BASE_DIR / "templates"],  # Dossier où chercher les templates personnalisés
        'APP_DIRS': True,  # Cherche automatiquement les templates dans chaque application
        'OPTIONS': {
            'context_processors': [  # Informations automatiquement passées aux pages
                'django.template.context_processors.debug',      # Infos de débogage
                'django.template.context_processors.request',    # Informations sur la requête
                'django.contrib.auth.context_processors.auth',   # Informations sur l'utilisateur
                'django.contrib.messages.context_processors.messages',  # Messages à afficher
>>>>>>> 3c75fe9 (project sahel_sahel stories-main)
            ],
        },
    },
]

<<<<<<< HEAD
# 🚀 Lanceur du serveur web
WSGI_APPLICATION = "sahel_api.wsgi.application"

# 🗄️ Base de données (utilise SQLite par défaut pour la simplicité)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # 🗃️ Type de base de données
        'NAME': BASE_DIR / 'db.sqlite3',         # 📊 Fichier de la base de données
=======
# 🚀 Application WSGI : point d'entrée pour le serveur web
WSGI_APPLICATION = "sahel_api.wsgi.application"

# 🗄️ Base de données : ici, on utilise un fichier simple (SQLite)
# Idéal pour le développement, facile à utiliser
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Type de base de données
        'NAME': BASE_DIR / 'db.sqlite3',         # Emplacement du fichier de la base
>>>>>>> 3c75fe9 (project sahel_sahel stories-main)
    }
}

# 🔐 Règles pour les mots de passe
<<<<<<< HEAD
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
=======
# Empêche les mots de passe trop simples
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        # Interdit les mots de passe trop proches du nom d'utilisateur
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        # Exige une longueur minimale
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        # Interdit les mots de passe trop courants (ex: "123456")
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        # Interdit les mots de passe composés uniquement de chiffres
    },
]

# 🌎 Langue et fuseau horaire
LANGUAGE_CODE = 'en-us'     # Langue par défaut : anglais
TIME_ZONE = 'UTC'           # Fuseau horaire : temps universel
USE_I18N = True             # Active la traduction (internationalisation)
USE_TZ = True               # Active l'utilisation des fuseaux horaires

# 🎨 Fichiers statiques : CSS, JavaScript, images fixes
STATIC_URL = '/static/'     # URL utilisée dans le navigateur pour accéder aux fichiers statiques
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Dossier où Django regroupe tous les fichiers statiques (pour la production)

# 📁 Dossier supplémentaire pour les fichiers statiques (pendant le développement)
if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / "static"]  # Où trouver les fichiers statiques en local

# 📸 Fichiers médias : fichiers uploadés par les utilisateurs (ex: photos)
MEDIA_URL = '/media/'       # URL pour accéder aux fichiers uploadés
MEDIA_ROOT = BASE_DIR / 'media'  # Dossier sur le serveur où stocker ces fichiers

# 🆔 Type de champ automatique par défaut pour les nouvelles bases de données
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 📦 Configuration de l'API REST (pour échanger des données)
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'  # Permet de filtrer les données
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [  # Méthodes pour vérifier qui accède à l'API
        'rest_framework.authentication.SessionAuthentication',  # Connexion via session
        'rest_framework.authentication.TokenAuthentication',    # Connexion via jeton (token)
    ],
    'DEFAULT_PERMISSION_CLASSES': [  # Qui a le droit d'accéder à l'API ?
        'rest_framework.permissions.IsAuthenticated',  # Seulement les utilisateurs connectés
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # Pagination
    'PAGE_SIZE': 10  # Nombre d'éléments affichés par page
}

# 🌳 Configuration pour accéder à Google Sheets (feuilles de calcul)
# Chemin vers le fichier de credentials (identifiants) pour accéder à Google
GOOGLE_SHEETS_CREDS = os.getenv(
    "GOOGLE_SHEETS_CREDS",  # Lu depuis .env
    str(BASE_DIR / "google-credentials.json")  # Fichier par défaut si non précisé
)

# Nom de la feuille Google Sheets à utiliser
GOOGLE_SHEETS_NAME = os.getenv(
    "GOOGLE_SHEETS_NAME",  # Lu depuis .env
    "Sahel Tree Planting"  # Nom par défaut
>>>>>>> 3c75fe9 (project sahel_sahel stories-main)
)