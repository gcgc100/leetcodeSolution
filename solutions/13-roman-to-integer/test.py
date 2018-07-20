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

    def test_roman_to_int(self):
        s = Solution()
        self.assertEqual(s.romanToInt("III"), 3)
        self.assertEqual(s.romanToInt("IV"), 4)
        self.assertEqual(s.romanToInt("IX"), 9)
        self.assertEqual(s.romanToInt("LVIII"), 58)
        self.assertEqual(s.romanToInt("MCMXCIV"), 1994)
        self.assertEqual(s.romanToInt("MCDLXXVI"), 1476)
        self.assertEqual(s.romanToInt("MMMCDIII"), 3403)
        self.assertEqual(s.romanToInt("MMCCCVII"), 2307)
        print s.romanToInt("MMCCCVMII")

    def test_previous_one(self):
        print Solution().previousOne("X")
