#!/usr/bin/python3
"""Decimal to binary and hexadecimal converter


This program will ask the user to input a decimal number and this program will
convert it into a binary and print it out and convert the binary back to
decimal and print out. It will do the same thing for hexadecimal as well.
"""


def to_decimal(number, base):
    """Convert a number to decimal from another base

    Convert a number from any base into decimal.

    Args:
        number: A string representing a number in base 2 to 16.
        base: The base of the number.

    Returns:
        An integer in base 10 of the number provided

    """
    converter = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    decimal = 0
    pos = 0
    while number:
        # Extract digits from the back of the number
        digit = number[-1]
        number = number[:-1]
        # Get the actual number in case it's an alphabet
        if converter.get(digit, None):
            digit = converter[digit]
        else:
            digit = int(digit)
        # Perform the multiplications
        decimal += (base ** pos) * digit
        pos += 1
    return decimal


def to_base(number, base):
    """Convert a decimal to another other base.

    Convert a base 10 number to any base from 2 to 16.

    Args:
        number: A decimal number.
        base: The base of the provided number.

    Returns:
        A string with the number in a requested base.

    """
    # Hold a conversion dict for ease of lookups
    converter = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F',
    }
    # A list to hold each character before conversion
    store = []
    while number > 0:
        # The reminder is the digit
        digit = number % base
        number = number // base
        if converter.get(digit, None):
            # Lookup the corresponding alphabet
            store.append(converter[digit])
        else:
            store.append(str(digit))
    # Reverse the list before joining and printing
    store.reverse()
    return ''.join(store)


def main():
    """The main function of the program.

    Requests input and calls the bin_convert and hex_convert functions.

    Returns:
        None. The outputs are printed to stdout.

    """
    num = input("Provide a number ")
    if not num.isalnum():
        print(f"{num} is not alphanumeric")
        return
    src_base = input("What is the base for this number? ")
    if not src_base.isnumeric():
        print(f"{src_base} is not a number")
        return
    dest_base = input("What base would you like to convert to (2-16)? ")
    if not dest_base.isnumeric():
        print(f"{dest_base} is not a number")
        return
    if int(src_base) == int(dest_base):
        print("The source and destination are the same")
    if src_base != 10:
        number = to_decimal(num.strip(), int(src_base))
    if int(dest_base) == 10:
        converted = number
    else:
        converted = to_base(number, int(dest_base))
    print(f"{num} in base {src_base} is {converted} in base {dest_base}")


if __name__ == '__main__':
    main()
