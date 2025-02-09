from os import system
import pytube

url = str(input("Vídeo or Playlist URL: "))

def video(url):
    try:
        video = pytube.YouTube(url).streams.get_highest_resolution().download()
    except:
        print("Error")


def playlist(url):
    playlist = pytube.Playlist(url)
    print(f'Downloading: {playlist.title}')
    
    for video in playlist.videos:
        try:
            print(video.title)
            video.streams.get_highest_resolution().download()
        except:
            print("Error")


def thumbnail(url):
    video = pytube.YouTube(url).thumbnail_url
    print(video)

def main():
    thumbnail(url)
    
main()
    

