#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for stringly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """

        :l1: TODO
        :l2: TODO
        :returns: TODO

        """
        ret = None
        retHead = ret
        addOn = 0
        while l1 is not None:
            assert l2 is not None
            output = (l1.val + l2.val + addOn) % 10
            addOn = (l1.val + l2.val + addOn) / 10
            
            if retHead is None:
                retHead = ListNode(output)
                ret = retHead
            else:
                ret.next = ListNode(output)
                ret = ret.next
            l1 = l1.next
            l2 = l2.next
        return retHead
