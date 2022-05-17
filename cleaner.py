import os


class Cleaner:
    def __init__(self):
        pass

    def remove_original_downloaded_mp4(self):
        entries = os.listdir("./")
        for entry in entries:
            if entry[-4:] == ".mp4":
                os.remove(entry)
