#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from solution import Solution
from solution import ListNode

class TestSolution(unittest.TestCase):

    """Test"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_two_numbers(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        output = Solution().addTwoNumbers(l1, l2)

        outputNumbers = [7, 0, 8]
        i = 0
        while output is not None:
            self.assertEqual(output.val, outputNumbers[i])
            print output.val
            i = i + 1
            output = output.next
