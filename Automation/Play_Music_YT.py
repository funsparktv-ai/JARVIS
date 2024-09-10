import os
import yt_dlp
from googleapiclient.discovery import build
from pydub import AudioSegment
from pydub.playback import play

# YouTube API credentials (replace with your own API key)
YOUTUBE_API_KEY = 'AIzaSyCD29Bf3-ttqE2axeaUu9M21RU5NzpIrYE'

# Path to ffmpeg executable
FFMPEG_PATH = r'F:\Python\ffmpeg-7.0.2-full_build\bin\ffmpeg.exe'
FFPROBE_PATH = r'F:\Python\ffmpeg-7.0.2-full_build\bin\ffprobe.exe'

# Setup YouTube client
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Set up environment for ffmpeg in pydub
os.environ["FFMPEG_BINARY"] = FFMPEG_PATH  # Explicitly set the ffmpeg path forpydub
os.environ["PATH"] += os.pathsep + r'F:\Python\ffmpeg-7.0.2-full_build\bin'


# Function to search for a YouTube video by song name
def search_youtube(track_name) :
    try :
        # Search for the track on YouTube
        request = youtube.search().list(
            part='snippet',
            q=track_name,
            type='video',
            maxResults=1
        )
        response = request.execute()

        # Extract the video ID from the search results
        if response['items'] :
            video_id = response['items'][0]['id']['videoId']
            video_title = response['items'][0]['snippet']['title']
            print(f"Found video: {video_title}")
            return video_id
        else :
            print("No video found.")
            return None
    except Exception as e :
        print(f"Error occurred while searching YouTube: {e}")
        return None


# Function to download and play YouTube audio
def play_youtube_audio(video_id) :
    ydl_opts = {
        'format' : 'bestaudio/best',
        'quiet' : True,
        'no_warnings' : True,
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
        'outtmpl' : 'audio.%(ext)s',
        'noplaylist' : True,
        'ffmpeg_location' : r'F:\Python\ffmpeg-7.0.2-full_build\bin',  # Path to ffmpeg directory
    }

    try :
        # Download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl :
            url = f'https://www.youtube.com/watch?v={video_id}'
            ydl.download([url])

        # Play the downloaded audio
        play_audio('audio.mp3')

    except Exception as e :
        print(f"Error occurred while downloading or playing audio: {e}")


# Function to play audio using pydub
def play_audio(file_path) :
    try :
        # Load the audio file
        audio = AudioSegment.from_mp3(file_path)
        print(f"Playing audio file: {file_path}")

        # Play the audio file
        play(audio)

    except Exception as e :
        print(f"Error occurred while playing audio: {e}")

def play_song(song_name):
    track_name = song_name
    video_id = search_youtube(song_name)
    if video_id:
        play_youtube_audio(video_id)