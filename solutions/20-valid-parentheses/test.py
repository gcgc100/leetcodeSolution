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

    def test_isvalid(self):
        s = Solution()
        self.assertTrue(s.isValid("[]"))
        self.assertFalse(s.isValid("]"))
