"""Module for working with real numbers
    
    This class creates numbers of the form a/b

    TODO: create a real from float numbers and irrational
"""
from discrete import gcd

class Real:
    """Comments
    """
    def __init__(self, r1 = 0, r2 = 1):
        a = b = c = d = 1

        if isinstance(r1, int):
            a = r1
            b = 1
        
        if isinstance(r1, float):
            number = str(r1)
            decimals = len(number.split(".")[1])
            a = r1*(10**decimals)
            b = 1*(10**decimals)

        if isinstance(r1, Real):
            a = r1.a
            b = r1.b

        if isinstance(r2, int):
            if r2 == 0:
                raise ZeroDivisionError
            c = r2
            d = 1

        if isinstance(r2, float):
            if r2 == 0:
                raise ZeroDivisionError
            number = str(r2)
            decimals = len(number.split(".")[1])
            c = r2*(10**decimals)
            d = 1*(10**decimals)

        if isinstance(r2, Real):
            c = r2.a
            d = r2.b

        self.a = a*d
        self.b = b*c
        self.simplify()

    def __add__(self, r):
        r = Real(r)
        b = self.b*r.b
        a = (b/self.b)*self.a + (b/r.b)*r.a
        return Real(a, b)

    def __sub__(self, r):
        r = Real(r)
        b = self.b*r.b
        a = (b/self.b)*self.a - (b/r.b)*r.a
        return Real(a, b)

    def __mul__(self, r):
        r = Real(r)
        b = self.b*r.b
        a = self.a*r.a
        return Real(a, b)

    def __truediv__(self, r):
        r = Real(r)
        b = self.b*r.a
        a = self.a*r.b
        return Real(a, b)

    def __eq__(self, r):
        r = Real(r)
        if self.a == r.a and self.b == r.b:
            return True
        else:
            return False

    def __repr__(self):
        if self.b == 1:
            return f'{self.a}'
        else:
            return f'{self.a}/{self.b}'

    def get_decimal(self):
        return self.a/self.b

    def simplify(self):
        if (self.a < 0 and self.b < 0) or self.a == 0:
            self.a = abs(self.a)
            self.b = abs(self.b)

        _gcd = gcd(abs(self.a), abs(self.b))

        self.a //= _gcd
        self.b //= _gcd

        self.a = int(self.a)
        self.b = int(self.b)
