#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:43:13 2019

@author: sbulut
"""

import random

SIZE = 52

# Create the deck of cards.
deck = list(range(SIZE))

l = list(range(SIZE))
l.reverse()

# Shuffle the deck of cards
for swaps in l:
    posn1 = random.randint(0, swaps)
    # Swap the cards at posn1 and posn2
    (deck[posn1], deck[swaps]) = (deck[swaps], deck[posn1])

print("shuffled deck is: ", deck)

# Create the empty hand.
hand = []

# Deal 5 cards from the deck into the hand.
for card in range( 0, 5 ):
    hand.append( deck.pop() )