from pytube import YouTube , Playlist

link = "https://youtu.be/d56sf29tSzw"

video = YouTube(link)

video.streams.get_highest_resolution().download(output_path='D:\Projects\python projects')

def finish():
    print("finished downloading ")
    
video.register_on_complete_callback(finish())


# for downloading playlists

#videos = Playlist(link)