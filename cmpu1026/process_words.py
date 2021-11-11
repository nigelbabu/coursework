#!/usr/bin/python3

VOWELS = ['a', 'e', 'i', 'o', 'u']

def words():
    with open('word_list.txt') as f:
        for line in f:
            yield line.strip()

def main():
    for word in words():
        pos = 0
        for letter in word:
            if letter in VOWELS:
                if letter == VOWELS[pos]:
                    pos += 1
                if pos == len(VOWELS):
                    break
        if pos >= 3:
            print(word)


if __name__ == '__main__':
    main()
