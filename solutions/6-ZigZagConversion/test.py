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

    def test_convert(self):
        inputStr = "PAYPALISHIRING"

        outputStr = Solution().convert(inputStr, 3)
        self.assertEqual(outputStr, "PAHNAPLSIIGYIR")
        outputStr = Solution().convert(inputStr, 4)
        self.assertEqual(outputStr, "PINAASRGYHPLII")
