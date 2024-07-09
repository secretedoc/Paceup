from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import re

# Load environment variables from .env file
load_dotenv()

def get_playlist_videos(playlist_id):
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the YOUTUBE_API_KEY environment variable.")
    
    youtube = build('youtube', 'v3', developerKey=api_key)

    videos = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part='contentDetails,snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            title = item['snippet']['title']
            video_id = item['contentDetails']['videoId']
            video_request = youtube.videos().list(
                part='contentDetails',
                id=video_id
            )
            video_response = video_request.execute()
            duration = video_response['items'][0]['contentDetails']['duration']

            # Convert duration to seconds
            hours = minutes = seconds = 0
            match = re.match(r'PT((?P<hours>\d+)H)?((?P<minutes>\d+)M)?((?P<seconds>\d+)S)?', duration)
            if match:
                if match.group('hours'):
                    hours = int(match.group('hours'))
                if match.group('minutes'):
                    minutes = int(match.group('minutes'))
                if match.group('seconds'):
                    seconds = int(match.group('seconds'))
            total_seconds = hours * 3600 + minutes * 60 + seconds
            videos.append((title, total_seconds))

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return videos
