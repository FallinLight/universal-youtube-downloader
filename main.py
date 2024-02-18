from pytube import YouTube, Stream
from sys import argv
import threading
import time
import os

def percent(tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

def get_highest_resolution(link):
         print(YouTube(link).streams.get_highest_resolution().resolution)
         return YouTube(link).streams.get_highest_resolution().resolution

#def progress_function(stream, chunk, bitesRemaining):
#        size = stream.filesize
#        
#        progress = percent(bitesRemaining, size)
#
#        return progress
    

class YoutubeDownload:

    def __init__(self):
        self.progress = 0
        self.thread: threading.Thread

    def download_link(self, link, download_type = "Video", resolution = "240p"):
        
        def progressFunction(stream, chunk, bitesRemaining):
            self.progress = 100 - percent(bitesRemaining, stream.filesize)

        yt = YouTube(link, on_progress_callback=progressFunction)

        print("Title: ", yt.title)
        print("Views: ", yt.views)

        if(download_type == "Video"):
            stream = yt.streams.get_by_resolution(resolution=resolution)
        else:
             stream = yt.streams.get_audio_only()

        out_file = stream.download("./")
        file_name = yt.title
        self.stream = stream

        if download_type == "Audio":
            base, ext = os.path.splitext(out_file)
            new_file = base + ".mp3"
            os.rename(out_file, new_file)

    
    def download_link_async(self, link, download_type = "Video", resolution = "240p"):
        download_thread = threading.Thread(target=self.download_link, name="Downloader", args=[link, download_type, resolution])
        self.thread = download_thread
        self.thread.start()
    
#download = YoutubeDownload()

#download.download_link_async("https://www.youtube.com/watch?v=fuLkcBxB8v0")

#otherDownload = YoutubeDownload()

#otherDownload.download_link_async("https://www.youtube.com/watch?v=Pcrkw4VLrcM")

