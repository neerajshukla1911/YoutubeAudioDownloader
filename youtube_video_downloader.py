from pytube import YouTube  
from pytube import Playlist
from pathlib import Path
import os

class YoutubeVideoDownloader:
    def __init__(self) -> None:
        pass

    def download(self, link, path):
        yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        print(f"Downloading {yt.title}")
        out_file = yt.streams.get_lowest_resolution().download(output_path=path)
        p = Path(out_file)
        name, ext = p.name.split('.')
        video_file_path = p.parent.joinpath(name + '.mp4')
        os.rename(out_file, video_file_path)
        return video_file_path
