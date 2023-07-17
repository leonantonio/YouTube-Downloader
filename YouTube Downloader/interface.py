#Antonio Leon 03/26/2023
#Last updated 06/26/2023
from tkinter import *
import tkinter as tk
from pytube import YouTube
import subprocess
import sys

#Window.
window = Tk()
window.geometry("800x600")
window.title("YouTube Downloader")
icon = PhotoImage(file = "C:\\Users\\jose-\\OneDrive\\Documentos\\Python Programs\\Youtube Download\\icon.png")
window.iconphoto(True, icon)

#Canvas.
canvas1 = tk.Canvas(window, width = 775, height = 30, bg = "#1D6BA8")
canvas1.pack()

canvas2 = tk.Canvas(window, width = 775, height = 50, bg = "#258CDB" )
canvas2.pack()

canvas3 = tk.Canvas(window, width = 775, height = 480, bg = "#C8E3EE")
canvas3.pack()

canvas4 = tk.Canvas(window, width = 775, height = 480, bg = "#C8E3EE")

def about_canvas():
    if canvas3.winfo_ismapped():
        canvas3.pack_forget()
        canvas4.pack()
    else:
        canvas4.pack_forget()
        canvas3.pack()

def video_information():
    url = entry_box.get()
    ytvideo = YouTube(url)
    title = ytvideo.title
    views = ytvideo.views
    file = ytvideo.streams.get_highest_resolution()
    file_size = file.filesize / 1000000
    channel_name = ytvideo.author
    thumbnail = ytvideo.thumbnail_url
    
    label_video_information = Label(canvas3,
                                    text="Title: " + title + "\nViews: "+ str(views) + "\nSize: "+str(file_size) + " MB" + "\nBy: "+channel_name, wraplength=700,
                                    font=("times new roman", 15),
                                    bg="#166694",
                                    )
    canvas3.create_window(400, 180, window=label_video_information)
    
    download_button = Button(canvas3,
                         text= "Download Video",
                         command= download_video
                         )
    canvas3.create_window(400, 300, window=download_button )
    
    download_button2 = Button(canvas3,
                         text= "Download Audio",
                         command= download_audio
                         )
    canvas3.create_window(400, 330, window=download_button2 )

def download_video():
    url = entry_box.get()
    ytvideo = YouTube(url)
    file = ytvideo.streams.get_highest_resolution()
    file.download("C:\\Users\\jose-\\Downloads\\Downloaded")
    
    done_label = Label(canvas3,
                       text=("Your video was downloaded :)"),
                       bg="#166694",
                       )
    canvas3.create_window(400, 400, window=done_label)
    
def download_audio():
    url = entry_box.get()
    ytvideo = YouTube(url)
    file = ytvideo.streams.get_audio_only()
    file.download("C:\\Users\\jose-\\Downloads\\Downloaded")
    
    done_label = Label(canvas3,
                       text=("Your audio was downloaded :)"),
                       bg="#166694",
                       )
    canvas3.create_window(400, 400, window=done_label)
    
def reset_button():
    window.destroy()
    subprocess.Popen([sys.executable] + sys.argv)

def delete_button():
    entry_box.delete(0,END)  
    
#Label for title.
label_title = Label(canvas2,
                   text= (f"YouTube Downloader"),
                   font= ("times new roman", 25),
                   bg= "#258CDB")
canvas2.create_window(400, 28, window=label_title)

#Entry box button.
entry_box = Entry(canvas3,
                  width= 35,
                  font= ("roboto", 18),
                  borderwidth=1,
                  )
entry_box.insert(0, "Enter URL video here")
entry_box.config(fg="grey")
canvas3.create_window(400, 60, window=entry_box)

#Delete button. 
delete_button = Button(canvas3,
                       text="Delete",
                       width=31, height=1,
                       command=delete_button,
                       )
canvas3.create_window(285, 91, window=delete_button)

#Enter button.
enter_button = Button(canvas3,
                      text="Enter",
                      width=31, height=1,
                      command=video_information
                      )
canvas3.create_window(515, 91, window=enter_button)

#Reset button.
reset_button = Button(canvas1,
                      text="Reset",
                      width=5, height=1,
                      bg="#1D6BA8",
                      relief="flat",
                      command=reset_button,
                      )
canvas1.create_window(30, 17, window=reset_button)

#About button.
about_button = Button(canvas1,
                      text="About",
                      width=5, height=1,
                      bg="#1D6BA8",
                      relief="flat",
                      command=about_canvas
                      )
canvas1.create_window(80, 17, window=about_button)

about_text = tk.Text(canvas4, height=20, width=90)
canvas4.create_window(388, 230, window=about_text)
text = """Welcome to our new YouTube downloader app, the perfect tool for downloading your 
favorite YouTube videos as MP4 or MP3 files. With our easy-to-use interface, you can 
quickly and easily convert any video from YouTube to the format of your choice and 
save it to your device for offline viewing or listening. Whether you want to listen to 
your favorite music on the go, watch a tutorial video offline, or save a documentary for 
later, our YouTube downloader app is here to help. Our app is safe, fast, and reliable, 
and you can download and convert as many videos as you like without any limitations. So, 
if you're looking for a hassle-free way to download YouTube videos in MP4 or MP3 
format, look no further than our app. Download it today and start enjoying your favorite 
videos offline!



Released in March, 2023
By Antonio Leon
Last updated June 26, 2023



Version 1.4"""
about_text.insert("2.0", text)
about_text.configure(state="disabled")




window.mainloop()