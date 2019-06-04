#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 22:00:37 2019

@author: sbulut
"""

import random

# why dicts?1

def dice_roll(sides=6):
    return random.randint(1,sides)
    
d = {2:     29,
     3:     66,
     4:     71,
     5:     100,
     6:     137,
     7:     173,
     8:     132,
     9:     122,
     10:    78,
     11:    59,
     12:    33
     }

rollsum = dice_roll() + dice_roll()

d[rollsum] = d[rollsum] + 1



# working with dictionary type
len(d)      # returns number of items in d
d.keys()    # returns a view of keys in d
d.values()  # returns a view of values in d
k in d      # returns True if k in d 
d[k]        # returns value associated with key k   
d[k] = v    # associates value v with key k
del d[k]    # removes entry with key k from d
d.pop(k)    # remove entry with key k but get value
for k in d: # iterate over keys in d

    
books = { "The C Programming Language": ['Brian W. Kernighan',
                                         'Dennis M. Ritchie'],
          "Harry Potter and the Philosopher's Stone" : ['J. K. Rowling'],
          "The AWK programming language" : ['Alfred V. Aho',
                                            'Brian W. Kernighan',
                                            'Peter J. Weinberger'],
          "The practice of programming": ['Brian W. Kernighan', 'Rob Pike']
          "The cat in the hat": ['Dr. Seuss'],
          "The UNIX Programming Environment": ['Brian W. Kernighan',
                                               'Rob Pike'],
        }













