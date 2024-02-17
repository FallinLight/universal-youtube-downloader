import PySimpleGUI as sg
from tkinter import *
import customtkinter
from main import YoutubeDownload, get_highest_resolution
import time
import threading

downloads = []

root = customtkinter.CTk()
root.title("Universal Youtube Downloader")
root.geometry("480x300")

resolutions = ["240p", "360p", "480p", "720p", "1080p"]
effectiveRes = resolutions

link = StringVar()

############## DOWNLOAD PROMPT ####################

root.grid_columnconfigure(0, weight=1)
frame = customtkinter.CTkFrame(master=root)
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

linkInput = customtkinter.CTkEntry(master=frame, height=25, placeholder_text="Link goes here...", textvariable=link)
linkInput.grid(row=0, column=0, padx=20, pady=20,sticky="ew")
#linkInput.place(anchor = CENTER, relx = 0.5, rely = 0.25)

progress_bar = customtkinter.CTkProgressBar(master=frame, orientation="horizontal")
progress_bar.set(0)
progress_bar.grid(row=2, column=0, padx=25, pady=25)
#progress_bar.place(anchor = CENTER, relx = 0.5, rely = 0.75)


def async_download():
    linkVal = linkInput.get()
    download = YoutubeDownload()
    downloads.append(download)
    download.download_link_async(linkVal)

button = customtkinter.CTkButton(master=frame, text="Download", command=async_download)
button.grid(row=1, column = 0, padx=25, pady=0, sticky="ew")
#button.place(anchor = CENTER, relx = 0.5, rely = 0.5)


############## SETTINGS SELECT ####################

root.grid_columnconfigure(1, weight=0)
settings_frame = customtkinter.CTkFrame(master=root)
settings_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsw")

resolution_dropdown = customtkinter.CTkOptionMenu(master=root, values=effectiveRes)
resolution_dropdown.grid(row=0, column=1, padx=10, pady=10)

linkProxy = linkInput.get()

def resetResList():
    print(link.get())
    maxRes = get_highest_resolution(link=link.get())
    effectiveRes = ["240p", "360p", "480p", "720p", "1080p"]

    for r in resolutions:
        print(r)
        if int(r.removesuffix("p")) > int(maxRes.removesuffix("p")):
            print(r)
            effectiveRes.remove(r)

    resolution_dropdown.configure(values=effectiveRes)

def link_callback(*args):
    newThread = threading.Thread(target=resetResList, name="Slambino")
    newThread.start()

link.trace_add(mode="write", callback=link_callback)

def second_loop():
    if(downloads):
        for x in downloads:
            progress_bar.set(x.progress / 100)
            print(x.progress)
            if x.progress >= 100:
                downloads.remove(x)
                x.thread.join()

    root.after(200, second_loop)

root.after(2000, second_loop)
root.mainloop()