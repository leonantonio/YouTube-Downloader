#Antonio Leon 03/12/2023
#Last update 06/26/2023
from tkinter import *
import tkinter as tk
from pytube import YouTube
import subprocess
import sys

window = Tk()
window.geometry("800x700")
window.title("Youtube Downloader")
window.config(background="white")

icon = PhotoImage(file="C:\\Users\\jose-\\OneDrive\Documentos\\Python Programs\\Youtube Download\\icon.png")
window.iconphoto(True, icon)

label = Label(window, text="\nYouTube Downloader Desktop App \n",
              font=("cascadia code", 23),
              bg="white")
label.pack()

def reset():
    window.destroy()
    subprocess.Popen([sys.executable] + sys.argv)

def videoInformation():
    url = entry.get()
    
    ytVideo = YouTube(url)
    
    title = ytVideo.title 
    views = ytVideo.views
    file = ytVideo.streams.get_highest_resolution()
    fileSizes = file.filesize / 1000000
    channelName = ytVideo.author
    thumbnail = ytVideo.thumbnail_url


    label_2 = Label(window, 
                    text="Title: " + title + "\nViews: "+ str(views) + "\nSize: "+str(fileSizes) + "\nBy: "+channelName, wraplength=700,
                    font=("times new roman", 15), 
                    bg="#f5f5f5",
                    )
    
    label_2.pack()
   
    donwload_button.pack()
    download_mp3_button.pack() 

def downloadVideo():
    url = entry.get()
    ytVideo = YouTube(url)
    file = ytVideo.streams.get_highest_resolution()
    file.download("C:\\Users\\jose-\Downloads\\Mp4 Downloaded")    
    done_label.pack()
    
def downloadMp3():
    url = entry.get()
    ytVideo = YouTube(url)
    mp3File = ytVideo.streams.get_audio_only()
    mp3File.download("C:\\Users\\jose-\\Downloads\\Mp3 Downloaded")
    done_label2.pack()
      
def delete():
    entry.delete(0, END)

def new_window():
    new_window = tk.Toplevel()
    new_window.geometry("420x420")
    new_window.title("About YouTube Downloader")
    text = Text(new_window, height=300, width=300)
    text.insert(END, "Welcome to our new YouTube downloader app, the \nperfect tool for downloading your favorite YouTube \nvideos as MP4 or MP3 files. With our easy-to-use \ninterface, you can quickly and easily convert any \nvideo from YouTube to the format of your choice and save it to your device for offline viewing or \nlistening.\n", 
                END, "\nWhether you want to listen to your favorite music \non the go, watch a tutorial video offline, or save \na documentary for later, our YouTube downloader app is here to help. Our app is safe, fast, and \nreliable, and you can download and convert as \nmany videos as you like without any limitations.\n",
                END, "\nSo, if you're looking for a hassle-free way to \ndownload YouTube videos in MP4 or MP3 format, look \nno further than our app. Download it today and \nstart enjoying your favorite videos offline!\n",
                END, "\n\nby Antonio Leon March 2023\n",
                END, "\nVersion 1.0")
    
    new_font = ("cascadia code", 10)
    text.configure(state=DISABLED, font=new_font)
    text.pack()
    
entry = Entry(window,
              width= 30,
              font=("roboto", 17),
              borderwidth=4, relief="ridge")
entry.insert(0, "Enter URL video here")
entry.config(fg="grey")
entry.pack()

enter_button = Button(window, 
                      text="Enter", 
                      command=videoInformation,
                      width=15, height=1,
                      relief="raised",
                      borderwidth=2)                 
enter_button.pack()


delete_button = Button(window,
                       text="Delete",
                       width=15, height= 1,
                       command=delete,
                       relief="raised",
                       )
delete_button.pack()

reset_button = Button(window,
                      text="Reset",
                      command=reset,
                      relief="flat",
                      )
reset_button.pack(side=RIGHT)


donwload_button = Button(window, text="Donwload Mp4", command=downloadVideo, width=15, height=2)
download_mp3_button = Button(window, text="Download Mp3", command=downloadMp3, width=15, height=2)

done_label = Label(text="Your Mp4 file was downloaded :)")
done_label2 = Label(text="Your Mp3 file was donwloaded :)")

new_window_button = Button(window, text="About", command=new_window, height=1, width=12, relief="flat", )
new_window_button.pack(side=BOTTOM)


window.mainloop()