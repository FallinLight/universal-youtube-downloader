from pytube import YouTube, Stream
from sys import argv
import threading
import time

def percent(tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc



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


    def download_link(self, link):
        
        def progressFunction(stream, chunk, bitesRemaining):
            self.progress = 100 - percent(bitesRemaining, stream.filesize)

        yt = YouTube(link, on_progress_callback=progressFunction)

        print("Title: ", yt.title)
        print("Views: ", yt.views)

        stream = yt.streams.get_highest_resolution()

        stream.download("./")
        self.stream = stream

    
    def download_link_async(self, link):
        download_thread = threading.Thread(target=self.download_link, name="Downloader", args=[link])
        self.thread = download_thread
        self.thread.start()
    
#download = YoutubeDownload()

#download.download_link_async("https://www.youtube.com/watch?v=fuLkcBxB8v0")

#otherDownload = YoutubeDownload()

#otherDownload.download_link_async("https://www.youtube.com/watch?v=Pcrkw4VLrcM")

