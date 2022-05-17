from itertools import accumulate
from pydub import AudioSegment
import os
import random
from cleaner import Cleaner


class audio_merger:
    def __init__(self, root_path):
        self.songs_folder_list_path = self.get_all_subfolders_path(root_path)
        self.aCleaner = Cleaner()

    def get_all_subfolders_path(self, root_path, exclude_mp3_flag=True):
        folders_list = []
        for file in os.listdir(root_path):
            if self.exclude_mp3(exclude_mp3_flag, file):  # exclude .mp3 files
                pass
            else:
                folders_list.append(root_path + "/" + file)
        return folders_list

    def exclude_mp3(self, exclude_mp3_flag, folder):
        return exclude_mp3_flag and (len(folder) >= 4) and (folder[-4:] == ".mp3")

    def merge_two_tracks(self, track_1_path, track_2_path, output_name):

        sound1 = AudioSegment.from_file(track_1_path, format="mp3")
        sound2 = AudioSegment.from_file(track_2_path, format="mp3")

        # Overlay sound2 over sound1 at position 0
        overlay = sound1.overlay(sound2, position=0)

        # simple export
        file_handle = overlay.export(output_name, bitrate="128k", format="mp3")

    def merge_except_instrument(self, audio_folder_path, instrument):
        """instrument = bass or vocals or drums or other"""

        print(f"Merging {audio_folder_path}...")
        # prepare list of stems path without instrument
        stems_list_path = self.get_all_subfolders_path(audio_folder_path, False)
        for stem_path in stems_list_path:
            if instrument in stem_path:
                stems_list_path.remove(stem_path)

        # merge
        print(f"Merging {stems_list_path[0]}...")
        accumulate_audio = AudioSegment.from_file(stems_list_path[0], format="mp3")
        for i in range(1, len(stems_list_path)):
            print(f"Merging {stems_list_path[i]}...")
            audio_file_to_merge = AudioSegment.from_file(
                stems_list_path[i], format="mp3"
            )

            accumulate_audio = accumulate_audio.overlay(audio_file_to_merge)

        output_name = f"{audio_folder_path} (without {instrument}).mp3"
        print(f"saving {output_name}...")
        accumulate_audio.export(output_name, bitrate="128k", format="mp3")

    def merge_all_subfolders_without_instrument(self, instrument):
        print(f"\n___MERGE___\n")
        for folder_path in self.songs_folder_list_path:
            self.merge_except_instrument(folder_path, instrument)
