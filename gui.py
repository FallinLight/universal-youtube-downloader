import PySimpleGUI as sg
from tkinter import *
import customtkinter
from main import YoutubeDownload
import time
import threading

downloads = []

root = customtkinter.CTk()
root.title("Universal Youtube Downloader")
root.geometry("480x300")

root.grid_columnconfigure(0, weight=1)
linkInput = customtkinter.CTkEntry(master=root, height=25, placeholder_text="Link goes here...")
linkInput.grid(row=0, column=0, padx=20, pady=20,sticky="ew")
#linkInput.place(anchor = CENTER, relx = 0.5, rely = 0.25)

progress_bar = customtkinter.CTkProgressBar(master=root, orientation="horizontal")
progress_bar.set(0)
progress_bar.grid(row=2, column=0, padx=25, pady=25)
#progress_bar.place(anchor = CENTER, relx = 0.5, rely = 0.75)


def async_download():
    linkVal = linkInput.get()
    download = YoutubeDownload()
    downloads.append(download)
    download.download_link_async(linkVal)

button = customtkinter.CTkButton(master=root, text="Download", command=async_download)
button.grid(row=1, column = 0, padx=25, pady=0, sticky="ew")
#button.place(anchor = CENTER, relx = 0.5, rely = 0.5)


def second_loop():
    if(downloads):
        for x in downloads:
            progress_bar.set(x.progress / 100)
            print(x.progress)
            if x.progress >= 100:
                downloads.remove(x)
                x.thread.join()

    root.after(500, second_loop)

root.after(2000, second_loop)
root.mainloop()