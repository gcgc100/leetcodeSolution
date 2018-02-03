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

    def test_is_match(self):
        s = Solution()
        self.assertEqual(s.isMatch("aa","a"), False)
        self.assertEqual(s.isMatch("aa","aa"), True)
        self.assertEqual(s.isMatch("aaa","aa"), False)
        self.assertEqual(s.isMatch("aa", "a*"), True)
        self.assertEqual(s.isMatch("aa", ".*"), True)
        self.assertEqual(s.isMatch("ab", ".*"), True)
        self.assertEqual(s.isMatch("aab", "c*a*b"), True)
        self.assertEqual(s.isMatch("aaa", "a.a"), True)
        self.assertEqual(s.isMatch("", "bab"), False)
        self.assertEqual(s.isMatch("aa", "."), False)
        self.assertEqual(s.isMatch("a", "ab*"), True)
        self.assertEqual(s.isMatch("a", "ab*a"), False)
        self.assertEqual(s.isMatch("b", "b.*c"), False)
        self.assertEqual(s.isMatch("", "c*c*"), True)
        self.assertEqual(s.isMatch("aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*"), True)
