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

    def test_reverse(self):
        t1 = 123
        s = Solution()
        self.assertEqual(s.reverse(t1), 321)
        t2 = -123
        self.assertEqual(s.reverse(t2), -321)
        t3 = 120
        self.assertEqual(s.reverse(t3), 21)
