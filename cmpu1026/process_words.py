#!/usr/bin/python3

VOWELS = ['a', 'e', 'i', 'o', 'u']

def words():
    with open('word_list.txt') as f:
        for line in f:
            yield line.strip()

def get_vowels(word):
    vowel_only = []
    for letter in word:
        if letter in VOWELS:
            vowel_only.append(letter)
    return vowel_only

def test_word(word):
    if len(word) < 6:
        return False
    if get_vowels(word) == VOWELS:
        return True
    return False

def main():
    for word in words():
        if test_word(word):
            print(word)


if __name__ == '__main__':
    main()
