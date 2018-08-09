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
    
    def test_count_and_say(self):
        s = Solution()
        self.assertEqual(s.countAndSay(3), "21")
        self.assertEqual(s.countAndSay(4), "1211")
        self.assertEqual(s.countAndSay(5), "111221")
