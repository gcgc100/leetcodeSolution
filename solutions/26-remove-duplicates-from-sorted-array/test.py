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

    def test_remove_duplicates(self):
        s = Solution()
        nums = [1,1,2]
        l = s.removeDuplicates(nums)
        self.assertEqual(l, 2)
        self.assertEqual(tuple(nums), tuple([1,2]))
        nums = [0,0,1,1,1,2,2,3,3,4]
        l = s.removeDuplicates(nums)
        self.assertEqual(l, 5)
        self.assertEqual(tuple(nums), tuple([0,1,2,3,4]))
