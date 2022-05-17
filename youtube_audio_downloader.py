from pytube import YouTube
from concurrent_manager import *


class Youtube_audio_downloader:
    def __init__(self, input_file):
        self.input_file_name = input_file
        self.url_list = []

    def parse_list(self):
        input_file = open(self.input_file_name, "r")
        while True:
            link = input_file.readline()  # Get next link from file
            if not link:  # if line is empty or end of file is reached
                break
            self.url_list.append(link)
        input_file.close()

    def run(self):
        self.parse_list()
        a_concurrent_manager = Concurrent_mananger()
        print("\n___DOWNLOAD___\n")
        a_concurrent_manager.concurrent_run(
            self.url_list, self.download_youtube_video_to_mp4
        )

    def download_youtube_video_to_mp4(self, link):
        yt = YouTube(link)
        print(f"Downloading: {yt.title}...")
        stream = yt.streams.filter(only_audio=True, audio_codec="mp4a.40.2")
        stream.last().download()
