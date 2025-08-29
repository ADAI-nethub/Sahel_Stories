# stories/google_sheets.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings


def get_google_sheet():
    """
    📊 Connect to one Google Sheet and return the first worksheet.
    """

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        settings.GOOGLE_SHEETS_CREDS, scope
    )

    client = gspread.authorize(creds)

    # Always use the first worksheet of the named sheet
    sheet = client.open(settings.GOOGLE_SHEETS_NAME).sheet1
    return sheet


