#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    Given a string s, find the longest palindromic substring in s.
    Maximum length is 1000
    """

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestPalindromeStr = ""
        for mid in range(1, len(s)):
            for blen in range(1, min(len(s)-mid, mid+1)):
                testStr = s[mid-blen: mid+blen+1]
                # from nose.tools import set_trace; set_trace()
                if testStr[0] == testStr[-1]:
                    if(len(longestPalindromeStr) < blen*2):
                        longestPalindromeStr = testStr
                else:
                    testStr = s[mid-blen: mid+blen]
                    if testStr[0] == testStr[-1]:
                        if(len(longestPalindromeStr) < blen*2):
                            longestPalindromeStr = testStr
                    else:
                        break
        if longestPalindromeStr == "" and len(s) > 0:
            longestPalindromeStr = s[0]

        return longestPalindromeStr
