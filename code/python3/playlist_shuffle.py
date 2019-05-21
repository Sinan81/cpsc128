# playlist_shuffle.py


import random

nsongs = eval(input("How many songs are in the playlist?"))

playlist=[]
while len(playlist) < nsongs:
    song = random.randint(1,nsongs)
    if song not in playlist:
        playlist.append(song)

print(playlist)