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

    def test_maxArea(self):
        s = Solution()
        r = s.maxArea([1,2,1])
        self.assertEqual(r, 2)
        r = s.maxArea([1,1])
        self.assertEqual(r, 1)
        r = s.maxArea([1,3,3])
        self.assertEqual(r, 3)
        r = s.maxArea([1])
        self.assertEqual(r, 0)
