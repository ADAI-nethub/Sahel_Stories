# Fichier : stories/google_sheets.py

import gspread  # Bibliotheque pour parler aux Google Sheets
from google.oauth2.service_account import Credentials  # Pour l'authentification
from django.conf import settings  # Pour acceder aux parametres de Django

from oauth2client.service_account import ServiceAccountCredentials

def get_google_sheet():
    """
    Cette fonction se connecte a une Google Sheet et retourne la premiere feuille de calcul.
    """

    # On definit les autorisations dont on a besoin

    scope = [
    'https://spreadsheets.google.com/feeds', # Permission pour lire les feuilles
    'https://www.googleapis.com/auth/drive'  # Permission pour acceder au Drive
]
    credentials = Credentials.from_service_account_file('your-credentials.json', scopes=scope)
    client = gspread.authorize(credentials)

    # On charge les identifiants de connexion depuis le fichier JSON
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        settings.GOOGLE_SHEETS_CREDS,  # Chemin vers le fichier d'identifiants
        scope  # Les autorisations demandees
    )

    # On cree un client autorise avec nos identifiants
    client = gspread.authorize(creds)

    # On ouvre la feuille de calcul par son nom et on prend la premiere feuille
    sheet = client.open(settings.GOOGLE_SHEETS_NAME).sheet1
    
    # On retourne la feuille de calcul pour pouvoir l'utiliser
    return sheet