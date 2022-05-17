import os
import subprocess
from datetime import date
from concurrent_manager import *


class Spleeter:
    def __init__(self):
        self.mp4_list = self.mp3_and_mp4_finder()
        self.stems_qty = 5
        self.folder_name = date.today().strftime("%Y-%m-%d") + "_separated_stems"
        self.execute_command_base = (
            "spleeter separate -c mp3 -o "
            + self.folder_name
            + f" -p spleeter:{self.stems_qty}stems"
        )

    def mp3_and_mp4_finder(self):
        output_list = []
        dir = "./"  # search in current directory
        entries = os.listdir(dir)
        for file in entries:
            newFile = self.song_renamer(file)
            if ".mp" in newFile:  # .mp3, mp4 etc
                output_list.append(newFile)
        return output_list

    def song_renamer(self, song):
        new_name = song.replace("(", "[").replace(")", "]")  # .replace(" ","")
        os.rename(song, new_name)
        return new_name

    def run(self):
        a_concurrent_manager = Concurrent_mananger()
        print("\n___SPLIT___")
        a_concurrent_manager.concurrent_run(self.mp4_list, self.split)

    def split(self, song):
        print(f"\nSeparating: {song}")
        subprocess.call(self.execute_command_base + ' "' + song + '"', shell=True)
        # os.remove(song)

    def serial_split(self):
        for song in self.mp4_list:
            self.split(song)
