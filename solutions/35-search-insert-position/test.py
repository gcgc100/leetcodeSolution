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

    def test_seartch_insert(self):
        s = Solution()
        self.assertEqual(s.searchInsert([1,3,5,6], 5), 2)
        self.assertEqual(s.searchInsert([1,3,5,6], 2), 1)
        self.assertEqual(s.searchInsert([1,3,5,6], 7), 4)
        self.assertEqual(s.searchInsert([1,3,5,6], 0), 0)
        self.assertEqual(s.searchInsert([1,3], 2), 1)
