#!/usr/bin/env python

from collections import Counter
import string

def frequency(words):
    """Calculates the relative letter frequency in the given words

    Words can be either a string or a collection of strings.
    The result is between 0.0 and 1.0, with 1.0 being the most frequent
    letter."""
    c = Counter()
    if type(words) == str:
        words = [words]

    for word in words:
        word = word.strip()
        word = word.upper()
        c.update(word)

    max_count = 0
    for letter in string.ascii_uppercase:
        if letter in c and c[letter] > max_count:
            max_count = c[letter]

    freq = {}
    for letter in string.ascii_uppercase:
        if max_count != 0:
            freq[letter] = c[letter] / float(max_count)
        else:
            freq[letter] = 0

    return freq

def compare_frequencies(freq1, freq2):
    """Compares two sets of letter frequencies and scores the result

    The result is a number between 0 and 100, 100 meaning the frequencies
    are the same."""
    sim = 0.0
    for letter in string.ascii_uppercase:
        sim += abs(freq2[letter] - freq1[letter])

    return 100 - (sim / 26) * 100

