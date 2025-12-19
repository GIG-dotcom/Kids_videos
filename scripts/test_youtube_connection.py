import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

CLIENT_ID = os.environ["YT_CLIENT_ID"]
CLIENT_SECRET = os.environ["YT_CLIENT_SECRET"]
REFRESH_TOKEN = os.environ["YT_REFRESH_TOKEN"]

SCOPES = [
    "https://www.googleapis.com/auth/youtube.readonly"]

creds = Credentials(
    token=None,
    refresh_token=REFRESH_TOKEN,
    token_uri="https://oauth2.googleapis.com/token",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    scopes=SCOPES,   # ✅ SCOPES MUST BE HERE
)

# Force token refresh with scopes
creds.refresh(Request())

youtube = build("youtube", "v3", credentials=creds)

request = youtube.channels().list(
    part="id,snippet",
    mine=True
)

response = request.execute()

print("✅ YouTube connection successful")
print("📺 Channel ID:", response["items"][0]["id"])
print("📺 Channel Name:", response["items"][0]["snippet"]["title"])
