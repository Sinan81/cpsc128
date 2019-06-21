# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 16:31:02 2019

@author: sbulut
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
    
if __name__ == '__main__':

    print( factorial(3) )