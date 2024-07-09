# main.py

from youtube_api import get_playlist_videos
from utils import calculate_total_duration, calculate_daily_video_goal, progress_recommendation

def main():
    playlist_url = input("Enter the YouTube playlist URL: ")
    playlist_id = playlist_url.split("list=")[-1]

    videos = get_playlist_videos(playlist_id)
    total_duration = calculate_total_duration(videos)
    daily_goal = float(input("Enter your daily goal (hours): "))
    daily_video_goal = calculate_daily_video_goal(total_duration, daily_goal, videos)
    
    print(f"Total playlist duration: {total_duration:.2f} hours")
    print(f"Daily video goal: {daily_video_goal} videos/day")

    while True:
        current_day = int(input("Enter the current day: "))
        user_progress = int(input("Enter the number of videos you've watched so far: "))
        
        recommendation = progress_recommendation(current_day, daily_video_goal, user_progress, videos)
        print(recommendation)
        
        if input("Do you want to continue? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()
