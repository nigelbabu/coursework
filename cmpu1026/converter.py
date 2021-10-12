#!/usr/bin/python3

def bin_convert(n):
    if n < 0:
        print(f"{n} is negative")
        return
    if n == 0:
        print(f"Binary: {n}")
        return

    binstore = []
    while n >= 1:
        binstore.append(str(n % 2))
        n = n // 2
    binstore.reverse()
    binary = ''.join(binstore)
    print('Binary:', binary)

    decimal = 0
    pos = 0
    while binary:
        digit = int(binary[-1])
        binary = binary[:-1]
        decimal += (2 ** pos) * digit
        pos += 1
        
    print('Decimal:', decimal)


def hex_convert(n):
    if n < 0:
        print(f"{n} is negative")
        return
    if n <10:
        print(f"Hexadecimal: {n}")
        return
    int_to_hex = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
    hexstore = []
    while n >= 1:
        digit = n % 16
        n = n // 16
        if digit < 10:
            hexstore.append(str(digit))
        else:
            hexstore.append(int_to_hex[digit])
    hexstore.reverse()
    hexadecimal = ''.join(hexstore)
    print('Hexadecimal:', hexadecimal)

    decimal = 0
    pos = 0
    hex_to_int = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    while hexadecimal:
        digit = hexadecimal[-1]
        hexadecimal = hexadecimal[:-1]
        if hex_to_int.get(digit, None):
            digit = hex_to_int[digit]
        else:
            digit = int(digit)
        decimal += (16 ** pos) * digit
        pos += 1
    print('Decimal:', decimal)




def main():
    num = input("Provide a decimal numer ")
    bin_convert(int(num))
    hex_convert(int(num))


if __name__ == '__main__':
    main()
