# playing_cards_skeleton_3.py
class Card:
    pass #not sure what to put here yet

class Deck:
    def __init__(self):
        self.cards = []
        for cardnum in range(52):
            self.cards.append(Card(cardnum))
    def shuffle(self):
        pass
    def cards_left(self):
        pass
    def deal(self, n=1):
        pass
    def __str__(self):
        return '' #can't use pass here

class Hand:
    def __init__(self):
        pass
    def add(self, cards):
        pass
    def size(self):
        pass
    def is_flush(self):
        pass
    def __str__(self):
        return '' #can't use pass here

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
