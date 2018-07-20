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

    def test_longestCommonPrefix(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(["flower","flow","flight"]), "fl")
