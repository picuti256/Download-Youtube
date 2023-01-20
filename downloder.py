# Biblioteca Pytube para baixar o video
from pytube import YouTube

# Função para baixar o video  
def download(link):
    video = YouTube(link)
    video = video.streams.get_highest_resolution()
    title = video.title
    if input (f"Do you really want to make the download? {title}? (y/n) ") == 'y':
        try:
            video.download()
            print("Success")
        except:
            print("Sorry, a unexpect error occurs")

link = input("Input the video URL: ")
download(link)