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

    def test_is_palindrome(self):
        a1 = 1771
        a2 = 292
        a3 = 1432
        s = Solution()
        self.assertTrue(s.isPalindrome(a1))
        self.assertTrue(s.isPalindrome(a2))
        self.assertTrue(not s.isPalindrome(a3))
