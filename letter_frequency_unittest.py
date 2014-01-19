#!/usr/bin/env python

import unittest
from letter_frequency import frequency

class TestFrequency(unittest.TestCase):
    def testFrequency_empty(self):
        freq = frequency("")
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertEquals(freq[letter], 0)

    def testFrequency_alpha(self):
        freq = frequency("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertEquals(freq[letter], 1)

    def testFrequency_a(self):
        freq = frequency("a")
        self.assertEquals(freq['A'], 1)
        for letter in "BCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertEquals(freq[letter], 0)

    def testFrequency_ab(self):
        freq = frequency("ab")
        self.assertEquals(freq['A'], 1)
        self.assertEquals(freq['B'], 1)
        for letter in "CDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertEquals(freq[letter], 0)

    def testFrequency_aab(self):
        freq = frequency("aab")
        self.assertEquals(freq['A'], 1)
        self.assertEquals(freq['B'], 0.5)
        for letter in "CDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertEquals(freq[letter], 0)

    def testFrequency_aabb(self):
        freq = frequency("aabb")
        self.assertEquals(freq['A'], 1)
        self.assertEquals(freq['B'], 1)
        for letter in "CDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertEquals(freq[letter], 0)
