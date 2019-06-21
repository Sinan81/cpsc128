# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:29:00 2019

@author: sbulut
"""


#with open('hellox.txt','r') as f:
#    for line in f:
#        print(line)


try:
    with open('hellox.txt','r') as f:
        for line in f:
            print(line)


except FileNotFoundError:
    print("Caught it!")