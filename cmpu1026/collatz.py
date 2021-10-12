#!/usr/bin/python3
import argparse


def main(n):
    while n > 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3*n) + 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Collatz conjecture')
    parser.add_argument('number', type=int)
    args = parser.parse_args()
    main(args.number)
