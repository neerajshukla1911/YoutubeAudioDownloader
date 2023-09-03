from pytube import YouTube  
from pytube import Playlist
import os
import ssl
from pathlib import Path
from youtube_video_downloader import YoutubeVideoDownloader
from video_to_audio_converter import VideoToAudioConverter
from constansts import ffmpeg_path
from songs_collection.krishna import video_base_path, audio_base_path, download_links
# from songs_collection.ganesha import video_base_path, audio_base_path, download_links
# from songs_collection.dahihandi import video_base_path, audio_base_path, download_links

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    if not os.path.exists(audio_base_path):
        os.makedirs(audio_base_path)

    if not os.path.exists(video_base_path):
        os.makedirs(video_base_path)

    for link_dir in download_links:
        if link_dir["download"]:
            video_file_path = YoutubeVideoDownloader().download(link_dir["link"], video_base_path)
            name, ext = Path(video_file_path).name.split('.')
            audio_file_path = Path(audio_base_path).joinpath(name + '.mp3')
            VideoToAudioConverter(ffmpeg_path).convert(video_file_path, audio_file_path)

if __name__ == '__main__':
    main()