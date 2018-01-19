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

    def test_two_sum(self):
        nums = [2, 7, 11, 15]
        target = 9

        self.assertEqual(Solution().twoSum(nums, target), [0, 1])
