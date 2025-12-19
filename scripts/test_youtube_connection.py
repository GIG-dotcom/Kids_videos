import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

creds = Credentials(
    None,
    refresh_token=os.environ["YT_REFRESH_TOKEN"],
    token_uri="https://oauth2.googleapis.com/token",
    client_id=os.environ["YT_CLIENT_ID"],
    client_secret=os.environ["YT_CLIENT_SECRET"],
    scopes=["https://www.googleapis.com/auth/youtube.upload"],
)

creds.refresh(Request())

youtube = build("youtube", "v3", credentials=creds)

print("✅ OAuth token is valid for YouTube UPLOAD")
