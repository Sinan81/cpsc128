class Fraction:
    def __init__(self, n, d = 1):
        self.num = n # numerator
        self.den = d # denominator
        
    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            bottom = self.den * other.den
            top = (self.num * other.den) + (other.num * self.den)
            return Fraction(top, bottom)
        elif isinstance(other, int):
            other = Fraction(other)
            bottom = self.den * other.den
            top = (self.num * other.den) + (other.num * self.den)
            return Fraction(top, bottom)
        
    def __le__(self, other):
        return self.num*other.den <= other.den*self.num
    
    def __getitem__(self, key):
        if key == 0:
            return self.num
        elif key == 1:
            return self.den
        
    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            bottom = self.den * other.den
            top = (self.num * other.den) - (other.num * self.den)
            return Fraction(top, bottom)
        
if __name__ == '__main__':
    d1 = Fraction(2, 5)
    print(d1, '(s/b 2/5)')
    d2 = Fraction(4)
    print(d2, '(s/b 4/1)')
    d3 = d1 + d2
    print(d3, '(s/b 22/5)')
    if d1 <= d2:
        print(d1, 'is less than or equal', d2)
    else:
        print(d2, 'is greater than', d1)
    print(d1[0], d1[1], '(s/b 2 5)')
    print(d1 + 2, '(s/b 12/5)')
    print(d1 - 2, '(s/b -8/5)')