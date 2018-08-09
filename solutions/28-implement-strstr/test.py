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

    def test_strStr(self):
        s = Solution()
        self.assertEqual(s.strStr("hello", "ll"), 2)
        self.assertEqual(s.strStr("aaaaa", "bba"), -1)
