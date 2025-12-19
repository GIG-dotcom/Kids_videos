import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

CLIENT_ID = os.environ.get("YT_CLIENT_ID")
CLIENT_SECRET = os.environ.get("YT_CLIENT_SECRET")
REFRESH_TOKEN = os.environ.get("YT_REFRESH_TOKEN")

if not CLIENT_ID or not CLIENT_SECRET or not REFRESH_TOKEN:
    raise Exception("❌ Missing YouTube secrets")

creds = Credentials(
    None,
    refresh_token=REFRESH_TOKEN,
    token_uri="https://oauth2.googleapis.com/token",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    scopes=["https://www.googleapis.com/auth/youtube.upload"]
)

youtube = build("youtube", "v3", credentials=creds)

request = youtube.channels().list(
    part="snippet",
    mine=True
)
response = request.execute()

channel = response["items"][0]["snippet"]["title"]

print("✅ YouTube connection successful")
print("📺 Channel name:", channel)
