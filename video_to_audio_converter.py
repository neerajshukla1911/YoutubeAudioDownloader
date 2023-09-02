import os


class VideoToAudioConverter:
    def __init__(self, ffmpeg_path) -> None:
        self.ffmpeg_path = ffmpeg_path

    def convert(self, video_file_path, audio_file_path):
        print(f"Converting ")
        os.system(f'{self.ffmpeg_path} -i "{video_file_path}" "{audio_file_path}"')
        print(f"Converted {video_file_path} to {audio_file_path}")
