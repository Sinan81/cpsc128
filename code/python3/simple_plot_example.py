#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:59:45 2019

@author: sbulut
"""

#example1
import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16],label='data by hand')
plt.ylabel('axis label with equation $y=x^2$')
plt.xlabel('x')
plt.legend()
plt.show()

#example 2
import numpy as np
import matplotlib.pyplot as plt
# search space (size of computational problem)
N=np.arange(1,20,0.5) #generates list: 1. 1.5 2 2.5 ...
plt.plot(N, N,label='linear search: $f(N)=N$')
plt.plot(N, np.log2(N), label='bisection method: $f(N)=log_2N$')
plt.ylabel('computation time')
plt.xlabel('problem size: N')
plt.legend()
plt.show()