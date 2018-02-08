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

    def test_length_of_longest_substring(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(Solution().lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring("c"), 1)
