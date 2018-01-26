#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Determine whether an integer is a palindrome. Do this without extra space.
    """

    def isPalindrome(self, x):
        """

        :type x: int
        :rtype: bool

        """
        if x<0 or (x!=0 and x%10 == 0):
            return False
        rev = 0
        while x>rev:
            rev = rev*10 + x%10
            x = x/10
        return x == rev or x == rev/10
