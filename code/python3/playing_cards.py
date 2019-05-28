#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 19:07:34 2019

@author: sbulut
"""

## playing_cards.py module v1
#SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
#FACE_VALUES = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
#               'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
#               'Queen', 'King')
#
#def suit(cardnum):
#    return SUITS[cardnum // 13]
#
#def face_value(cardnum):
#    return FACE_VALUES[cardnum % 13]
#
#def label(cardnum):
#    return face_value(cardnum) + " of " + suit(cardnum)
#
#print('My name is', __name__) # Line 24!
#card = 15
#print("Card", card, "is the", face_value(card), "of", suit(card))
#print("Card", card, "is the", label(card))

# playing_cards.py module v2
SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
FACE_VALUES = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
               'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
               'Queen', 'King')

def suit(cardnum):
    return SUITS[cardnum // 13]

def face_value(cardnum):
    return FACE_VALUES[cardnum % 13]

def label(cardnum):
    return face_value(cardnum) + " of " + suit(cardnum)

if __name__ == '__main__':
    card = 15   
    print("Card", card, "is the", face_value(card), "of", suit(card))
    print("Card", card, "is the", label(card))

    