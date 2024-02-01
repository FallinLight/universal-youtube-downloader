from pytube import YouTube
from sys import argv
import threading

def download_link(link):
    
    yt = YouTube(link)

    print("Title: ", yt.title)
    print("Views: ", yt.views)

    stream = yt.streams.get_highest_resolution()

    stream.download("./")

def download_link_async(link) -> threading.Thread:
    download_thread = threading.Thread(target=download_link, name="Downloader", args=[link])
    download_thread.start()
    return download_thread