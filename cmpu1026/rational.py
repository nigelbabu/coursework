#!/usr/bin/python3
"""Create a data structure for rational numbers

Create a class for rational numbers and methods to add, substract, and reduce a
fraction to its simplest form.
"""


class Fraction(object):
    
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def add(self, second):
        l = lcm(self.denominator, second.denominator)
        numerator = (
                self.numerator * (l // self.denominator) +
                second.numerator * (l // second.denominator))
        self.numerator = numerator
        self.denominator = l
        self.reduce()
        return self

    def subtract(self, second):
        l = lcm(self.denominator, second.denominator)
        numerator = (
                self.numerator * (l // self.denominator) -
                second.numerator * (l // second.denominator))
        print(numerator, l, self.denominator)
        self.numerator = numerator
        self.denominator = l
        self.reduce()
        return self

    def reduce(self):
        g = gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g


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


def main():
    one = Fraction(1, 4)
    two = Fraction(1, 4)
    print(lcm(4, 4))
    print(one.add(two))
    print(one.subtract(two))
    f = Fraction(3, 6)
    f.reduce()
    print(f)

if __name__ == '__main__':
    main()
