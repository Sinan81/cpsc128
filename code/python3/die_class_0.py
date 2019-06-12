# die_class_0.py
import random

class Die:
    def __init__(self, n):
        self.nsides = n
        
    def roll(self):
        spots = random.randint(1,self.nsides)
        return spots

if __name__ == '__main__':
    d1 = Die(6)
    red = Die(20)
    
    print('Rolling d1 ...', end='')
    result = d1.roll()
    print('result =', result)
    
    print('Rolling red and d1 together gets you:', d1.roll() + red.roll() )
    print('The die d1 has %d sides' % (d1.nsides) )