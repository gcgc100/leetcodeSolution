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
            v1 = l1.val
            if l2 is None:
                v2 = 0
            else:
                v2 = l2.val
            output = (v1 + v2 + addOn) % 10
            addOn = (v1 + v2 + addOn) / 10
            
            if retHead is None:
                retHead = ListNode(output)
                ret = retHead
            else:
                ret.next = ListNode(output)
                ret = ret.next
            l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        while l2 is not None:
            v1 = 0
            v2 = l2.val
            output = (v1 + v2 + addOn) % 10
            addOn = (v1 + v2 + addOn) / 10
            
            ret.next = ListNode(output)
            ret = ret.next
            l2 = l2.next
        if addOn == 1:
            ret.next = ListNode(1)
        return retHead
