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

    def test_remove_element(self):
        s = Solution()
        nums = [3,2,2,3]
        l = s.removeElement(nums, 3)
        self.assertEqual(l,2)
        self.assertEqual(tuple(nums[:l]), tuple([2,2]))
        nums = [0,1,2,2,3,0,4,2]
        l = s.removeElement(nums, 2)
        self.assertEqual(l,5)
        self.assertEqual(tuple(nums[:l]), tuple([0,1,3,0,4]))
