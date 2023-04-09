from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config import api_key

def get_authenticated_service(api_key):
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

youtube = get_authenticated_service(api_key)
