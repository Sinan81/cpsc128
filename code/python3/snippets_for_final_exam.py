#This code generates a playlist for a CD.
#The strategy is to start with an empty playlist,
#then generate random track numbers and
#add the track numbers to the playlist
#if they are not already in it.

import random
_______________ = eval(input('How many tracks are on the CD? '))
playlist = ___________
while ______________ < tracks:
    _________ = random.randint(1, tracks)
    if tracknum _________ playlist:
        playlist.__________(______________)

print(playlist)


class Window:
    def __init__(self, width, height, ball_list):
        self.width = width
        self.height = height
        self.balls = ball_list

    def detect_collisions(self):
        pass

class Ball:
    def __init__(self, p, v=0):
    self.posn = p
    self.velocity = v

class Position:
    def __init__(self, x, y):
    self.x = x
    self.y = y

# Initialize game:
ball_list = [ Ball(Position(10,10)), Ball(Position(2,3)),
Ball(Position(10,10)), Ball(Position(3,2)),
Ball(Position(5,5)), Ball(Position(5,5)),
Ball(Position(4,1)), Ball(Position(5,5)),
Ball(Position(4,1))
]
game = Window(80, 25, ball_list)
print( game.detect_collisions() )
