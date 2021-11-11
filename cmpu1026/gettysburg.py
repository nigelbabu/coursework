#!/usr/bin/python3

import requests
import string
import collections  


SPEECH_URL="https://markfoley.info/pa1/gettysburg.txt"
STOPWORDS_URL="https://markfoley.info/pa1/stopwords.txt"


def fetch(url):
    resp = requests.get(url)
    return resp.text


def split_into_words(speech):
    word = []
    words = []
    for letter in speech:
        if letter in string.punctuation or letter in string.whitespace:
            if len(word) > 0:
                words.append(''.join(word))
                word = []
                continue
        if (letter not in string.punctuation and letter not in
                string.whitespace):
            word.append(letter)
    return words


def clean_words(words, stop_words):
    cleaned = []
    for word in words:
        if word.lower() not in stop_words.split(','):
            cleaned.append(word)
    return cleaned


def main():
    # fetch the files
    speech = fetch(SPEECH_URL)
    words = split_into_words(speech)
    stop_words = fetch(STOPWORDS_URL)
    # clean the speech
    cleaned_speech = clean_words(words, stop_words)
    # get counts
    print(f"Total words: {len(cleaned_speech)}")
    c = collections.Counter(cleaned_speech)
    # get unique words
    unique_words = 0
    for word, count in c.items():
        if count == 1:
            unique_words += 1
    print(f"Unique words: {unique_words}")
    # count occurences of each word
    for word, count in c.items():
        print(f"{word}: {count}")


if __name__ == '__main__':
    main()
