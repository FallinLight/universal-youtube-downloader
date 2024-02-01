import PySimpleGUI as sg
import main

sg.theme("DarkAmber")

layout = [
    [sg.Text('Universal Youtube Downloader')],
    [sg.Text('Video Link: '), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Window Title', layout)

event, values = window.read()
window.close()

text_input = values[0]

downloadThread = main.download_link_async(text_input)
sg.popup('Your video is now downloading', text_input)

while downloadThread.is_alive:
    print("Test")

window.close()

sg.popup("Done!")
