from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

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
            hours = int(duration[2:].split('H')[0]) if 'H' in duration else 0
            minutes = int(duration.split('H')[-1].split('M')[0]) if 'M' in duration else 0
            seconds = int(duration.split('M')[-1].split('S')[0]) if 'S' in duration else 0
            total_seconds = hours * 3600 + minutes * 60 + seconds
            videos.append((title, total_seconds))

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return videos
