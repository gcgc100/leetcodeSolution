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

    def test_my_atoi(self):
        s = Solution()

        a1 = s.myAtoi("121")
        a2 = s.myAtoi("-1234")
        a3 = s.myAtoi("   123")
        a4 = s.myAtoi("012")
        self.assertRaises(Exception, s.myAtoi, "134.12")
        self.assertRaises(Exception, s.myAtoi, "-432.34")
        self.assertRaises(Exception, s.myAtoi, "as234")
        self.assertRaises(Exception, s.myAtoi, "214sdf")
        self.assertEqual(a1, 121)
        self.assertEqual(a2, -1234)
        self.assertEqual(a3, 123)
        self.assertEqual(a4, 12)
