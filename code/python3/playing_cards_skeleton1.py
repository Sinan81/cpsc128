# playing_cards_skeleton_1.py
class Deck:
    def __init__(self):
        pass            
    def shuffle(self):
        pass
    def cards_left(self):
        pass
    def deal(self, n=1):
        pass

class Hand:
    def __init__(self):
        pass
    def add(self, cards):
        pass
    def size(self):
        pass
    def is_flush(self):
        pass

d = Deck()
d.shuffle()
print('d after shuffling =', d)
print('d has', d.cards_left(), 'cards')
roxx = Hand()
chris = Hand()
for card in range(5):
    roxx.add(d.deal())
print('Your hand of', roxx.size(), 'cards contains:', roxx)
chris.add(d.deal(5))
print('Your hand of', chris.size(), 'cards contains:', chris)
print('There are', d.cards_left(), 'cards left in the deck.')
if roxx.is_flush():
    print('roxx rocks!')
