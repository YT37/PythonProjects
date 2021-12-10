import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def create(secret_file):
    print("Creating Service")
    SCOPES = ["https://www.googleapis.com/auth/youtube"]

    creds = None
    pickle_file = "Token.pickle"

    if os.path.exists(pickle_file):
        with open(pickle_file, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                secret_file,
                SCOPES,
            )
            creds = flow.run_local_server()

        with open(pickle_file, "wb") as token:
            pickle.dump(creds, token)

    service = build("youtube", "v3", credentials=creds)
    print("Created Service\n\n")

    return service
