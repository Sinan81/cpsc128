#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:43:13 2019

@author: sbulut
"""

import random

# Create the deck of cards.
deck = list(range(52))

# Shuffle the deck of cards
for swaps in range(104):
    posn1 = random.randint(0, 51)
    posn2 = random.randint(0, 51)
    # Swap the cards at posn1 and posn2
    (deck[posn1], deck[posn2]) = (deck[posn2], deck[posn1])

# Create the empty hand.
hand = []

# Deal 5 cards from the deck into the hand.
for card in range( 0, 5 ):
    hand.append( deck.pop() )