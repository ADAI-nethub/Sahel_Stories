import gspread
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run_flow
from oauth2client.file import Storage

# Your credentials from Google Cloud (OAuth 2.0 Client ID)
CLIENT_ID = 'your-client-id-here'
CLIENT_SECRET = 'your-client-secret-here'
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

flow = OAuth2WebServerFlow(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    scope=SCOPE,
    redirect_uri=REDIRECT_URI
)

# This will open a browser window for you to log in
storage = Storage('credentials.json')
credentials = run_flow(flow, storage)

print("Authentication successful. Credentials saved to credentials.json")