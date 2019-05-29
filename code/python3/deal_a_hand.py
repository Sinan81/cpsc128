# deal_a_hand.py
# This program deals a hand of 5 cards at random. 
# CPSC128 Example code
# S. Bulut 2019, T. Topper 2015

import random

# Define handy string constants.
FACE_VALUES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
               'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
               'Queen', 'King']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

# Create deck of cards.
deck = list(range(52))

# Create empty hand.
hand = []

# Deal 5 cards into hand.
for deal in range(5):
    posn = random.randint(0, len(deck) - 1)
    hand.append(deck[posn])
    del(deck[posn])

# Display the cards in the hand.
for card in hand:
    print(FACE_VALUES[card % 13], 'of', SUITS[card // 13])

