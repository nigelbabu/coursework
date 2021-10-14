#!/usr/bin/python3
"""Find the square root of a number by the Babylonian algorithm

1. Take a number, a guess, and a floating point tolerance.
2. Divide the number by the guess.
3. Average the quotient and the guess.
4. Make the new guess the average for step 5.
5. If the guess is within the floating point tolerance, print the answer.
"""


def main():
    # Get numbers from the user
    number_input = input("Provide a number ")
    guess_input = input("Provide a guess ")
    tolerance_input = input("Provide a floating point tolerance ")
    
    # Convert inputs to the correct types
    number = int(number_input)
    guess = int(guess_input)
    tolerance = float(tolerance_input)

    quotient = number//guess
    average = (guess + quotient) / 2
    remainder = average - guess
    count = 1
    if remainder < 0:
        remainder *= -1

    while remainder >= tolerance:
        print(f"You have unsuccessfully guessed sqrt({number}) with a "
              f"tolerance of {tolerance}, you were out by {remainder}. Please"
              " try again.")
        guess_input = input("Provide a guess ")
        guess = int(guess_input)
        quotient = number/guess
        average = (guess + quotient) / 2
        remainder = average - guess
        if remainder < 0:
            remainder *= -1
        count += 1

    print(f"You guessed the sqrt({number}) within a tolerance of {tolerance}"
          f" with {count} tries.")


    



if __name__ == '__main__':
    main()
