from flask import Flask, request, jsonify, send_from_directory
from youtube_api import get_playlist_videos
from utils import calculate_total_duration, calculate_daily_video_goal

app = Flask(__name__, static_folder='public', static_url_path='')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/playlist', methods=['GET'])
def get_playlist_data():
    playlist_id = request.args.get('playlistId')
    daily_goal = float(request.args.get('dailyGoal'))

    videos = get_playlist_videos(playlist_id)
    total_duration = calculate_total_duration(videos)
    daily_video_goal = calculate_daily_video_goal(total_duration, daily_goal, videos)

    return jsonify({
        'totalDuration': total_duration,
        'dailyVideoGoal': daily_video_goal
    })

if __name__ == '__main__':
    app.run(debug=True)
