#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 19:47:37 2019

@author: sbulut
"""

if cardnum == 0 or cardnum == 13 or cardnum == 26 or cardnum == 39 :
    face_value = 'Ace'
elif cardnum == 1 or cardnum == 14 or cardnum == 27 or cardnum == 40 :
    face_value = 'Two'


FACE_VALUES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', \
                'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

face_value = cardnum % 13
print('The face value of card number', cardnum, 'is', FACE_VALUES[face_value])

# convert from hand list to suit_list
suit_list = []
for card in hand:
    suit_list.append(card//13)
    

## is it a flush? Sol_1a
if suit_list[1] == suit_list[0] and suit_list[2] == suit_list[1] and \
    suit_list[3] == suit_list[2] and suit_list[4] == suit_list[3]:
    print("That's a flush!")
else:
    print("Sorry no flush here.")
    
## is it a flush? Sol_1b
flush = True # Start by assuming it is a flush.

# The first test compares the second card to the first card,
# so the initial previous card is the first card in the hand.
prev_card = suit_list[0]
for card in suit_list[1:]:
    # Note: To loop starting with the second card we use a slice of the list,
    # that begins in the second position, i.e. position #1.
    if card != prev_card: # If card's suit not the same as previous one's.
        flush = False # It's not a flush.
    prev_card = card # Update previous card: This card will be the previous 
                     # card next time around.
if flush:
    print("That's a flush!")
else:
    print("Sorry, no flush here.")
    

## Is it a flush? sol_1c
flush = True
for posn in range(1,len(suit_list)-1):
    if suit_list[posn] != suit_list[posn-1]:
        flush = False
        break

if flush:
    print("That's a flush!")
else:
    print("Sorry, no flush here.")


## Is it a flush? sol2
flush = False
for suit in [0,1,2,3]:
    count = 0
    for card_suit in suit_list:
        if card_suit == suit:
            count = count + 1
    if count == len(suit_list):
        flush = True
        break

if flush:
    print("That's a flush!")
else:
    print("Sorry, no flush here.")

## Is it a flush? sol3
if suit_list.count(suit_list[0]) == len(suit_list):
    print("That's a flush!")
else:
    print("Sorry, no flush here.")
    
## Is it a flush? sol4
suit_list.sort()
if suit_list[0] == suit_list[len(suit_list) - 1]:
    print("That's a flush!")
else:
    print("Sorry, no flush here.")
   
### poker hands: alternative representation
deck = [
['A','C'], ['2','C'], ['3','C'], ['4','C'], ['5','C'], ['6','C'], ['7','C'],
['8','C'], ['9','C'], ['10','C'], ['J','C'], ['Q','C'], ['K','C'],
['A','D'], ['2','D'], ['3','D'], ['4','D'], ['5','D'], ['6','D'], ['7','D'],
['8','D'], ['9','D'], ['10','D'], ['J','D'], ['Q','D'], ['K','D'],
['A','H'], ['2','H'], ['3','H'], ['4','H'], ['5','H'], ['6','H'], ['7','H'],
['8','H'], ['9','H'], ['10','H'], ['J','H'], ['Q','H'], ['K','H'],
['A','S'], ['2','S'], ['3','S'], ['4','S'], ['5','S'], ['6','S'], ['7','S'],
['8','S'], ['9','S'], ['10','S'], ['J','S'], ['Q','S'], ['K','S']]


### multi-dimensional
g = [ [ 'X', 'O', '' ], [ 'O', 'X', 'O' ], [ '', '', 'X'] ]

if g[0][0]==g[0][1] and g[0][1]==g[0][2]:
    print(g[0][0], 'has won!')
else:
    print('No one has won in the top row.')
    
    if g[0][0]==g[1][1] and g[1][1]==g[2][2]:
        print(g[0][0], 'has won!')
    else:
        print('No one has won on the main diagonal.')


    
    
# pallindrome sol1
palindrome = True
for offset in range(0, len(s)//2):
    if s[offset] != s[len(s)-1-offset]:
       palindrome = False
       break

if palindrome:
    print("It is a palindrome!")
else:
    print("It is NOT a palindrome.")
    
## pallindrome sol2
s = "madam"
slist = list(s)
slist.reverse()
s_reversed = ''.join(slist)
if s == s_reversed:
    print("It is a palindrome!")
else:
    print("It is NOT a palindrome.")

## pallindrome: preprocessing for phrases
s = "A man, a plan, a canal, Panama."
print(s, "becomes...",end='')
s_new = ''
for c in s:
    if c.isalpha():
        if c.isupper():
            s_new = s_new + c.lower()
        else:
            s_new = s_new + c
print(s_new)

###### modularization


# is_even complete example
import random

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
num = random.randint(0,100)
if is_even(num):
    print("Good news your magic number is even!\
    10 bonus points for you.")
else:
    print("Bad news, your magic number is odd.")
    

# Example dice_roll v1
import random

def dice_roll():
    return random.randint(1,6)

total = dice_roll() + dice_roll()
print("On your first roll you got:", total)

# Example dice_roll v2
import random

def dice_roll(sides):
    return random.randint(1,sides)

total = dice_roll(6) + dice_roll(6)
print("On your first roll you got:", total)

# Default arguments
import random

def dice_roll(sides = 6):
    return random.randint(1,sides)

print('Your results are:')
print('6-sided die:', dice_roll())
print('24-sided die:', dice_roll(24))

### functions for playing cards
SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
FACE_VALUES = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
               'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
               'Queen', 'King')

def suit(cardnum):
    return SUITS[cardnum // 13]

def face_value(cardnum):
    return FACE_VALUES[cardnum % 13]

card = 15
print("Card", card, "is the", face_value(card), "of", suit(card))

### playing cards with label function
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

card = 15
print("Card", card, "is the", face_value(card), "of", suit(card))
print("Card", card, "is the", label(card))


# blackjack.py
...
print 'You are holding,'
for card in hand:
    print('The', label(card))
... 

# blackjack.py
import playing_cards

hand = [15, 42, 8]
print('You are holding,')
for card in hand:
    print('The', playing_cards.label(card))
    
    
    
# playing_cards.py module v1
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

print('My name is', __name__) # Line 16!
card = 15
print("Card", card, "is the", face_value(card), "of", suit(card))
print("Card", card, "is the", label(card))

#import tricks

card=10

import playing_cards
print(playing_cards.label(card))

import playing_cards as pc
print(pc.label(card))

from playing_cards import label
print(label(card))

from playing_cards import *
print(label(card))

from playing_cards import label as card_name
print(card_name(card))


#### perils of immutability

# increment.py
def increment(n):
    n = n + 1

num = 48
increment(num)
print(num)

def increment(seq):
    seq.append(42)

lst = [48]
increment(lst)
print(lst)

l = [ 'Tim' ]
n = l
l.append( 'Joyce' )
print(l)
print(n)

a = 'Tim'
b = 'Tom'
lst = [b, a]
a = 'Matt'
lst[1] = lst[0]
print(lst)

# deep copy
import copy

g = [ [1,2], 3]

dc = copy.deepcopy(g)

dc[0][0] = 'x'

print(g)
print(dc)
