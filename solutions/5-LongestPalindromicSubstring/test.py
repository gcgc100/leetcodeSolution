#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from solution import Solution

class TestSolution(unittest.TestCase):

    """Test"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_longest_palingdrome(self):
        inputStr = "babad"
        outputStr = Solution().longestPalindrome(inputStr)
        self.assertEqual(outputStr, "bab")
        inputStr = "cbbd"
        outputStr = Solution().longestPalindrome(inputStr)
        self.assertEqual(outputStr, "bb")
        inputStr = "cbbb"
        outputStr = Solution().longestPalindrome(inputStr)
        self.assertEqual(outputStr, "bbb")
        inputStr = "cba"
        outputStr = Solution().longestPalindrome(inputStr)
        self.assertEqual(outputStr, "")
