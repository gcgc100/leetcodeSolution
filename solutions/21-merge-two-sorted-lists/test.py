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

    def test_mergeTwoLists(self):
        s = Solution()
        print s.mergeTwoLists([1,2,4], [2,3,6,7])
