#Antonio Leon 03/08/2023

from pytube import YouTube

print ("Download videos or Mp3 files from Youtube in the highets resolution available. \n")

url = input("Enter URL:")
ytVideo = YouTube(url)

title = ytVideo.title 
views = ytVideo.views
downloadVideo = ytVideo.streams.get_highest_resolution()
fileSizes = downloadVideo.filesize / 1000000
mp3 = ytVideo.streams.get_audio_only()

print ("\n", ytVideo.thumbnail_url)
print ("\nTitle: ", title, "\nViews: ", views, "\nSize on Megabytes: ", fileSizes, "\nResolution: ")

while True:
    
    userChoice = input("\nHow would yuo like to download this file? Mp3 or Video?: ").lower()
    if userChoice == "mp3":
        print ("\nWhere are converting your file to Mp3...")
        mp3.download("C:\\Users\\jose-\\Downloads")
        break
    elif userChoice == "video":
        print ("\nWhere are converting your file to Video...")
        downloadVideo.download("C:\\Users\\jose-\\Downloads")
        break
    else:
        print ("\nWrong input!")
        continue
        
print ("Done!")

exitt = input ("")
    
    
    
    



