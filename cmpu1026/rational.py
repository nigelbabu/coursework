#!/usr/bin/python3
"""Create a data structure for rational numbers

Create a class for rational numbers and methods to add, substract, and reduce a
fraction to its simplest form.
"""


class Fraction(object):
    
    def __init__(self, num, denom):
        self.frac = (num, denom)

    def __str__(self):
        return f"{self.frac[0]} / {self.frac[1]}"

def gcd(first, second):
    if first < second:
        tmp = first
        first = second
        second = tmp
    while second != 0:
       tmp = second
       second = first % second
       first = tmp
    return first

def lcm(first, second):
    if first == 0 and second == 0:
        return 0
    return (first // gcd(first, second)) * second


def addFrac(frac1, frac2):
    l = lcm(frac1.frac[1], frac2.frac[1])
    numerator = (
            frac1.frac[0] * (l // frac1.frac[1]) +
            frac2.frac[0] * (l // frac2.frac[1]))
    return Fraction(numerator, l)

def subFrac(frac1, frac2):
    l = lcm(frac1.frac[1], frac2.frac[1])
    numerator = (
            frac1.frac[0] * (l // frac1.frac[1]) -
            frac2.frac[0] * (l // frac2.frac[1]))
    return Fraction(numerator, l)

def reduce(frac):
    g = gcd(frac.frac[0], frac.frac[1])
    return Fraction(frac.frac[0] // g, frac.frac[1] // g)

def main():
    one = Fraction(1, 4)
    two = Fraction(1, 3)
    print(addFrac(one, two))
    print(subFrac(one, two))
    print(reduce(Fraction(3, 6)))

if __name__ == '__main__':
    main()
