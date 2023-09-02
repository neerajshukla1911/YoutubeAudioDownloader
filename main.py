from pytube import YouTube  
from pytube import Playlist
import os
import ssl
from pathlib import Path
from youtube_video_downloader import YoutubeVideoDownloader
from video_to_audio_converter import VideoToAudioConverter
from .krishna import video_base_path, audio_base_path, download_links


ssl._create_default_https_context = ssl._create_unverified_context

ffmpeg_path = '/Users/neeraj/binaries/ffmpeg'


for link_dir in download_links:
    if link_dir["download"]:
        video_file_path = YoutubeVideoDownloader().download(link_dir["link"], video_base_path)
        name, ext = Path(video_file_path).name.split('.')
        audio_file_path = Path(audio_base_path).joinpath(name + '.mp3')
        VideoToAudioConverter(ffmpeg_path).convert(video_file_path, audio_file_path)