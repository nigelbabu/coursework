#!/usr/bin/python3
"""Find the square root of a number by the Babylonian algorithm

1. Take a number, a guess, and a floating point tolerance.
2. Divide the number by the guess.
3. Average the quotient and the guess.
4. Make the new guess the average for step 5.
5. If the guess is within the floating point tolerance, print the answer.
"""
import math


def main():
    # Get numbers from the user
    number_input = input("Provide a number ")
    guess_input = input("Provide a guess ")
    tolerance_input = input("Provide a floating point tolerance ")
    
    # Convert inputs to the correct types
    number = int(number_input)
    guess = int(guess_input)
    tolerance = float(tolerance_input)

    while math.fabs(guess*guess - number) >= tolerance: 
        quotient = number/guess
        average = (quotient + guess) / 2
        guess = average

    print(guess)


    



if __name__ == '__main__':
    main()
