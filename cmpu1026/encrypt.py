#!/usr/bin/python3
"""Encrypt and decrypt a string with a simple algorithm.

To encrypt, reverse and increase the ASCII code by 1. To decrypt, do the
reverse.
"""

def encrypt(plain):
    output = []
    for char in plain:
        output.append(chr(ord(char)+1))
    output.reverse()
    return ''.join(output)


def decrypt(encrypted):
    output = []
    for char in encrypted:
        output.append(chr(ord(char)-1))
    output.reverse()
    return ''.join(output)

def main():
    plain = input("Enter some plain text ")
    print(f"Encrypting {plain}")
    encrypted = encrypt(plain)
    print(encrypted)
    encrypted = input("Enter some encrypted text ")
    print(f"Encrypting {encrypted}")
    plain = decrypt(encrypted)
    print(plain)

if __name__ == "__main__":
    main()
