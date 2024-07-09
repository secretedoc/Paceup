# utils.py

import math

def calculate_total_duration(videos):
    total_seconds = sum(duration for _, duration in videos)
    return total_seconds / 3600

def calculate_daily_video_goal(total_duration, daily_goal, videos):
    total_days = total_duration / daily_goal
    return math.ceil(len(videos) / total_days)

def progress_recommendation(current_day, daily_video_goal, user_progress, videos):
    ideal_completion = current_day * daily_video_goal

    if ideal_completion > user_progress:
        additional_videos = ideal_completion - user_progress
        return f"You're behind schedule. Try to watch {additional_videos} more videos today to catch up."
    elif ideal_completion == user_progress:
        return "You're on track! Keep up the good work."
    else:
        return f"You're ahead of schedule! Consider adjusting your daily goal or exploring supplementary materials."
