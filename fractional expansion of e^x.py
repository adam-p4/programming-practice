# Searches for fractional expansion of e^x with >=digits digits in the numerator (using Taylor Series)

from math import factorial 
from fractions import Fraction

x = 1
digits = 2

def texp(x, n): # nth expansion of taylor series of e^x
    res = 0
    for i in range(n+1):
        res += x**i / factorial(i)
    return Fraction(str(res)).limit_denominator(10**10)

for i in range(100): # test
    print(f'{texp(x, i)=}, ({i=})')
    if len(str(texp(x,i).numerator))>=digits:
        print("found")
        break
