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

        outputStr = Solution().convert("A", 1)
        self.assertEqual(outputStr, "A")
        outputStr = Solution().convert(inputStr, 3)
        self.assertEqual(outputStr, "PAHNAPLSIIGYIR")
        outputStr = Solution().convert(inputStr, 4)
        self.assertEqual(outputStr, "PINALSIGYAHRPI")
        outputStr = Solution().convert("ABC", 2)
        self.assertEqual(outputStr, "ACB")
        outputStr = Solution().convert("ABCD", 3)
        self.assertEqual(outputStr, "ABDC")
