import PySimpleGUI as sg
from tkinter import *
import customtkinter
from main import YoutubeDownload
import time
import threading

downloads = []

root = customtkinter.CTk()

linkInput = customtkinter.CTkTextbox(master=root)
linkInput.place(anchor = CENTER, relx = 0.5, rely = 0.75)

progress_bar = customtkinter.CTkProgressBar(master=root, orientation="horizontal")
progress_bar.set(0)
progress_bar.place(anchor = CENTER, relx = 0.5, rely = 1)

def async_download():
    linkVal = linkInput.get("0.0", "end")
    download = YoutubeDownload()
    downloads.append(download)
    download.download_link_async(linkVal)


button = customtkinter.CTkButton(master=root, text="Download", command=async_download)
button.place(anchor = CENTER, relx = 0.5, rely = 0.5)


def second_loop():
    if(downloads):
        progress_bar.set(downloads[0].progress / 100)
        print(downloads[0].progress)

    root.after(500, second_loop)
        

root.after(2000, second_loop)
root.mainloop()