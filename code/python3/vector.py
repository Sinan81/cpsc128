#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:18:04 2019

@author: sbulut
"""
from math import sqrt 

class Vector:
    def __init__(self,xlen,ylen):
        self.x = xlen
        self.y = ylen
        self.norm = sqrt(self.x**2 + self.y**2)
        
    def __str__(self):
        return str(self.x) + 'i + ' + str(self.y) + 'j'
    
    def __add__(self,other):
        if isinstance(other,Vector):
            return Vector(self.x + other.x, self.y + other.y)
        
    def __le__(self,other):
        return self.norm <= other.norm
    
    def __mul__(self,other):
        if isinstance(other,int):
            return Vector(other*self.x, other*self.y)

if __name__ == '__main__':
    v1 = Vector(1,2)
    print("v1 is: ", v1)
    print("v1.norm is: ", v1.norm)
    v2 = Vector(1,3)
    print("v2 is: ",v2)
    print("is v1 <= v2?: ", v1 <= v2)
    print("v1+v2 is: ", v1+v2)
    print("v1*2 is ", v1*2)
    
    
    
    