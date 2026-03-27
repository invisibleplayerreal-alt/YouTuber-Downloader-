import yt_dlp                                   #Library to download YouTube videos

url = input("Enter the URL: ")                  #Get YouTube video URL from user

ydl_opts = {
    'format': 'best',                           #Download parametr
    'outtmpl': 'Test.%(ext)s'                   #Test = video name, (extension added automatically)
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])                         #Download the video

print("Download Completed")                     #Notify when finished.