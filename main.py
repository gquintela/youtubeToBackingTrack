from youtube_audio_downloader import Youtube_audio_downloader
from split import Spleeter
from audio_merger import audio_merger
import sys


if (len(sys.argv) != 2) or sys.argv[1] not in ["vocals", "drums", "bass"]:
    print(
        "Usage: must include only one argument of the following: 'vocals', 'drums' or 'bass' to remove from tracks."
    )
    exit(0)

instrument_to_remove = sys.argv[1]
print(f"Instrument to remove: {instrument_to_remove}\n")

aDownloader = Youtube_audio_downloader("inputFile.txt")
aDownloader.run()

aSplitter = Spleeter()
folder_name = aSplitter.folder_name
aSplitter.serial_split()

an_audio_merger = audio_merger(folder_name)
an_audio_merger.merge_all_subfolders_without_instrument(instrument_to_remove)
an_audio_merger.aCleaner.remove_original_downloaded_mp4()
