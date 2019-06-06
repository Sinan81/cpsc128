import numpy as np
import matplotlib.pyplot as plt

#generate a list of x values to be fed to a function
#[1., 1.5, 2, 2.5 ...]
def f1(n):
    return 2*n**2 + n

def f2(n):
    return n**2 + n

#ap: alive percent
def f3(ap):
    return 4*ap*100 + 4

N = np.arange(1,100,1) 

plt.plot(N, f1(0*N + 100), label='option 1 $2n^2+n$')

plt.plot(N, f2(0*N + 100), label='option 2: $n^2+n$')

plt.plot(N, f3(N), label='option 3:$4x+4$ (x is alive cells)')

plt.ylabel('storage footprint (bytes)')
plt.xlabel('percentage of alive cells')
plt.title('100 x 100 system')
plt.legend()
plt.show()