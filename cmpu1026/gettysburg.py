#!/usr/bin/python3
"""Parse the gettysburg address and do word count analysis.
"""
import string
import requests


SPEECH_URL="https://markfoley.info/pa1/gettysburg.txt"
STOPWORDS_URL="https://markfoley.info/pa1/stopwords.txt"


def fetch(url):
    """Fetch a URL

    Arg:
        url: A string in the URL form.

    Returns:
        The response in text
    """
    resp = requests.get(url)
    return resp.text


def split_into_words(speech):
    """Split paragraphs into words

    Arg:
        speech: A string

    Returns:
        A list of words
    """
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
    """Remove stop words from words

    Args:
        words: A list of words
        stop_words: Comma separated string with stop words that should be
        removed from words.

    Returns:
        A list of words with stop words removed.
    """
    cleaned = []
    for word in words:
        if word.lower() not in stop_words.split(','):
            cleaned.append(word)
    return cleaned


def get_word_counts(words):
    """Count the number of times a word appears in the words dict

    Args:
        words: A list of words

    Returns:
        A dict with the word as key and the count as value
    """
    word_counts = {}
    for word in words:
        if word_counts.get(word) is None:
            word_counts[word] = 1
            continue
        word_counts[word] += 1
    return word_counts


def main():
    """The main function
    """
    # fetch the files
    speech = fetch(SPEECH_URL)
    words = split_into_words(speech)
    stop_words = fetch(STOPWORDS_URL)
    # clean the speech
    cleaned_speech = clean_words(words, stop_words)
    # get counts
    print(f"Total words: {len(cleaned_speech)}")
    #c = collections.Counter(cleaned_speech)
    word_counts = get_word_counts(cleaned_speech)
    # get unique words
    unique_words = 0
    for word, count in word_counts.items():
        if count == 1:
            unique_words += 1
    print(f"Unique words: {unique_words}")
    # count occurences of each word
    for word, count in word_counts.items():
        print(f"{word}: {count}")


if __name__ == '__main__':
    main()
