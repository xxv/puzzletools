#!/usr/bin/env python

import sys
import re
from letter_frequency import frequency, compare_frequencies

def caesar(chars, offset):
    chars = chars.upper()
    chars = re.sub(r"[^A-Z]+", "", chars)
    return "".join(map(lambda char: chr((((ord(char)-65) + offset) % 26) + 65), chars))

def all_caesar(chars, target_freq):
    """Goes through all the caesar cyphers of the input text, showing a score

    The score shown is based on the input frequency. The more "#" shown,
    the more it matches."""
    min_len = None
    caesars = []
    for i in range(0,26):
        word = caesar(chars, i)
        freq = frequency(word)
        score = compare_frequencies(freq, target_freq)
        caesars.append({ "word": word, "freq": freq, "score": score })
        if not min_len or min_len > int(score):
            min_len = int(score)

    for i in range(0,26):
        print i, caesars[i]["word"], "#" * (int(caesars[i]["score"]) - min_len)

def eng_freq():
    with open("/usr/share/dict/words") as f:
        return frequency(f)

if __name__== '__main__':
    all_caesar(sys.argv[1], eng_freq())
