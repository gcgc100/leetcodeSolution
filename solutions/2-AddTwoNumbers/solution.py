#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for stringly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    """
    Given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain 
    a single digit. Add the two numbers and return it as a linked list.
    """

    def addTwoNumbers(self, l1, l2):
        """

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

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
