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

    def test_max_sub_array(self):
        s = Solution()
        self.assertEqual(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(s.maxSubArray([-1]), -1)
        self.assertEqual(s.maxSubArray([-2, -1]), -1)
        self.assertEqual(s.maxSubArray([1]), 1)
