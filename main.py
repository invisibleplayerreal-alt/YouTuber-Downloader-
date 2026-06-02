import yt_dlp                                  

url = input("Enter the URL: ")                 

ydl_opts = {
    'format': 'best',                           
    'outtmpl': '%(title)s.%(ext)s'              
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])                  

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download Completed!")
except Exception as e:
    print(f"Download failed. Error: {e}")

                 



