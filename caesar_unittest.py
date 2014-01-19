#!/usr/bin/env python

import unittest
import string

from caesar import caesar

class TestCaesar(unittest.TestCase):
    def setUp(self):
        self.test_str = string.ascii_letters.upper()

    def testIdentity(self):
        result = caesar(self.test_str, 0)
        self.assertEqual(self.test_str, result)

    def testRot1(self):
        result = caesar(self.test_str, 1)
        self.assertEqual("BCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZA", result)

    def testRot13(self):
        result = caesar(self.test_str, 13)
        self.assertEqual("NOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM", result)

    def testRot26(self):
        result = caesar(self.test_str, 26)
        self.assertEqual(self.test_str, result)

    def testRot52(self):
        result = caesar(self.test_str, 52)
        self.assertEqual(self.test_str, result)

    def testFilter_uppercasing(self):
        result = caesar("abcde", 0)
        self.assertEqual("ABCDE", result)

    def testFilter_stripPunctuation(self):
        result = caesar("it's car!",0)
        self.assertEqual("ITSCAR", result)

if __name__ == '__main__':
    unittest.main()
