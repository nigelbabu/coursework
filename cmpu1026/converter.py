#!/usr/bin/python3
"""Decimal to binary and hexadecimal converter


This program will ask the user to input a decimal number and this program will
convert it into a binary and print it out and convert the binary back to
decimal and print out. It will do the same thing for hexadecimal as well.
"""
def bin_convert(number):
    """Perform binary conversion.

    Convert to binary and back to decimal from the binary string. Prints out both values

    Args:
        number: A decimal number.

    Returns:
	None. The outputs are printed to stdout.

    """
    if number < 0:
        print(f"{number} is negative")
        return
    if number == 0:
        print(f"Binary: {number}")
        print(f"Decimal: {number}")
        return

    # create a list to hold the individual digits of binary number
    binstore = []
    while number > 0:
        # Keep appending the remainders to the list
        binstore.append(str(number % 2))
        # Reduce the number down to smaller sizes
        number = number // 2
    # The reminders need to be reversed
    binstore.reverse()
    # Join the items of the list into one string
    binary = ''.join(binstore)
    print('Binary:', binary)

    decimal = 0
    pos = 0
    while binary:
        # Extract the last digit
        digit = int(binary[-1])
        # Pop the last digit from the binary
        binary = binary[:-1]
        # Convert each digit to decimal value
        decimal += (2 ** pos) * digit
        pos += 1
    print('Decimal:', decimal)


def hex_convert(number):
    """Perform hexadecimal conversion.

    Convert to hexadecimal and back to decimal from the hexadecimal string. Prints out both values

    Args:
        number: A decimal number.

    Returns:
	None. The outputs are printed to stdout.

    """
    if number < 0:
        print(f"{number} is negative")
        return
    if number <10:
        print(f"Hexadecimal: {number}")
        print(f"Decimal: {number}")
        return
    # Hold a conversion dict for ease of lookups
    int_to_hex = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
    # A list to hold each character before conversion
    hexstore = []
    while number > 0:
        # The reminder is the digit
        digit = number % 16
        number = number // 16
        # If the number does not have to be converted
        if digit < 10:
            hexstore.append(str(digit))
        else:
            # Lookup the corresponding alphabet
            hexstore.append(int_to_hex[digit])
    # Reverse the list before joining and printing
    hexstore.reverse()
    hexadecimal = ''.join(hexstore)
    print('Hexadecimal:', hexadecimal)

    decimal = 0
    pos = 0
    # Conversion dict that's reverse the previous one
    hex_to_int = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    while hexadecimal:
        # Extract digits from the back of the number
        digit = hexadecimal[-1]
        hexadecimal = hexadecimal[:-1]
        # Get the actual number in case it's an alphabet
        if hex_to_int.get(digit, None):
            digit = hex_to_int[digit]
        else:
            digit = int(digit)
        # Perform the multiplications
        decimal += (16 ** pos) * digit
        pos += 1
    print('Decimal:', decimal)


def main():
    """The main function of the program.

    Requests input and calls the bin_convert and hex_convert functions.

    Returns:
	None. The outputs are printed to stdout.

    """
    num = input("Provide a decimal numer ")
    bin_convert(int(num))
    hex_convert(int(num))


if __name__ == '__main__':
    main()
